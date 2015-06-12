#include <stdio.h>
#include "X.h"
#include "Xlib.h"
/*#include "misc.h"*/
#include "resource.h"
#define NEED_EVENTS
#define NEED_REPLIES
#include "Xproto.h"
#include "windowstr.h"
#include "inputstr.h"
#include "scrnintstr.h"
#include "cursorstr.h"

#include "NXlib.h"
#include "Events.h"
#include "window.h"
#include "Windows.h"
#include "windowstr.h"
#include "propertyst.h"
#include "dixstruct.h"
#include "Icons.h"
#include "Keyboard.h"
#include "Pointer.h"
#include "Rootless.h"
#include "Client.h"
#include "resource.h"
#include "Display.h"
#include "Screen.h"

#include "X11/Xlibint.h"

#include "NXlocalevents.h"

/* TODO remove */
#define DEBUG

/* TODO create a list of qvdRedirectEmbedder */
Window qvdRedirectEmbedder = -1;
static struct _redirectWindowList *redirectWindowList = NULL;

struct _redirectWindowList {
  Window w;
  struct _redirectWindowList *next;
};

/*
 * returns 1 if the window w is one of the windows that had the _QVD_REDIRECT_EVENT prop
 * and 0 otherwise
 */
int _isRedirectWindow(Window w)
{
  struct _redirectWindowList *ptr = redirectWindowList;

  for (ptr = redirectWindowList; ptr != NULL; ptr = ptr->next)
      if (ptr->w == w)
	return 1;

  return 0;
}

/*
 * Adds the window w to the redirect list
 * Returns 1 if the window already existed, and 0 otherwise
 */

int _addRedirectWindow(Window w)
{
  struct _redirectWindowList *ptr = redirectWindowList;
  struct _redirectWindowList *last = redirectWindowList;

  if (redirectWindowList == NULL)
    {
      redirectWindowList = malloc(sizeof(struct _redirectWindowList));
      redirectWindowList->w = w;
      redirectWindowList->next = NULL;
    }
  for (ptr = redirectWindowList; ptr != NULL; ptr = ptr->next)
      if (ptr->w == w)
	return 1;
      else
	last = ptr;

  last->next = malloc(sizeof(struct _redirectWindowList));
  if (last->next == NULL)
    {
      perror("Error allocating memory for Redirect window after setting _QVD_REDIRECT_EVENT xprop");
      exit(1);
    }
  last->next->w = w;
  last->next->next = NULL;
  return 0;
}

/*
 * Deletes the window w from the redirect list
 * Returns 1 if the window did not exist, and 0 if it was correctly removed
 */

int _delRedirectWindow(Window w)
{
  struct _redirectWindowList *ptr = redirectWindowList;

  if (redirectWindowList == NULL) {
    fprintf(stderr, "_delRedirectWindow: Unable to delete redirect window 0x%x from redirect list. Was it allocated before?\n", (unsigned) w);
    return 1;
  }
  if (redirectWindowList->w == w)
    {
      redirectWindowList = redirectWindowList->next;
      free(ptr);
      return 0;
    }

  struct _redirectWindowList *last = redirectWindowList;

  for (ptr = redirectWindowList->next; ptr != NULL; ptr = ptr->next)
      if (ptr->w == w)
	{
	  last->next = ptr->next;
	  free(ptr);
	  return 0;
	}
      else
	last = ptr;

  fprintf(stderr, "_delRedirectWindow: Unable to delete redirect window 0x%x from redirect list. Was it allocated before?\n", (unsigned) w);

  return 1;
}

#define MAXREDIRECTBUFFER 512
char redirectwindowbuffer[MAXREDIRECTBUFFER];
char *_dumpQvdRedirectEmbedder() {
  struct _redirectWindowList *ptr = redirectWindowList;
  redirectwindowbuffer[0] = '\0';
  /*  char *tempbuffer[MAXREDIRECTBUFFER]; */

  for (ptr = redirectWindowList; ptr != NULL; ptr = ptr->next)
    snprintf(redirectwindowbuffer, MAXREDIRECTBUFFER, "%s,0x%x",  redirectwindowbuffer, (unsigned)(ptr->w));

  redirectwindowbuffer[MAXREDIRECTBUFFER - 1] = '\0';
  return redirectwindowbuffer;
}

/* 
 * DeliverLocalEventsToQvdWindow
 *
 * If an event is sent to a window signaled with the property _QVD_REDIRECT_EVENT
 * Then each time the cursor enters the window the input window is lowered, and 
 * each time the window is left the input window is raised again
 *
 */
int DeliverLocalEventsToQvdWindow(register WindowPtr pWin, xEvent *pEvents)
{
  int type = pEvents->u.u.type;
  Window w = nxagentWindowPriv(pWin)->window;

  

  if (!_isRedirectWindow(w))
    {
#ifdef DEBUG
      fprintf(stderr, "The window is not used to redirect 0x%x, qvdRedirectEmbedder %s\n", (unsigned int)w, _dumpQvdRedirectEmbedder());
#endif
      return 0;
    }


  Window remote = nxagentWindowPriv(pWin)->window;

  switch(type)
    {
    case EnterNotify:
      {
	int lowerres = XLowerWindow(nxagentDisplay, nxagentInputWindows[pWin->drawable.pScreen->myNum]);
#ifdef DEBUG
	fprintf(stderr, "XLowerWindow after event %d result for display %s and window 0x%x, 0x%x was %d\n",
		type, nxagentDisplay->display_name, 
		(unsigned) w,
		(unsigned) nxagentInputWindows[pWin->drawable.pScreen->myNum], lowerres);
#else
	(void)lowerres; /* No warnings */
#endif
	break;
      }
    case DestroyNotify:
      {
	/* TODO remove the window from the list of redirect windows */
	/* TODO map pWin to window id */
	fprintf(stderr, "Remove window from list 0x%x remote 0x%x\n", (unsigned) pWin->drawable.id, (unsigned)remote);
	_delRedirectWindow(remote);
      }
    case LeaveNotify:
    case NoExpose:
    case UnmapNotify:
    case ReparentNotify:
    case GravityNotify:
    case ResizeRequest:
    case CirculateNotify:
    case CirculateRequest:
      {
	int raiseres = XRaiseWindow(nxagentDisplay, nxagentInputWindows[pWin->drawable.pScreen->myNum]);
#ifdef DEBUG
	fprintf(stderr, "XRaiseWindow result for event type %d for display %s and window 0x%x was %d\n",
		type, nxagentDisplay->display_name,
		(unsigned) nxagentInputWindows[pWin->drawable.pScreen->myNum], raiseres);
#else
	(void)raiseres; /* No warnings */
#endif
	break;
      }
    }


  return 0;
}

int ChangeWindowPropertyQvdRedirectEvent(WindowPtr pWin, Atom property)
{
    Atom qvdRedirect = MakeAtom(QVD_REDIRECT_XPROP, strlen(QVD_REDIRECT_XPROP), True);
    if (property == qvdRedirect)
      {

        Window remote = nxagentWindowPriv(pWin)->window;
	_addRedirectWindow(remote);
#ifdef DEBUG
	fprintf(stderr, "Enabling window 0x%x to have direct window access, bypassing NX input window\n",
		(unsigned int)remote);
#endif

      }

  return 0;
}


int DeleteWindowPropertyQvdRedirectEvent(WindowPtr pWin, Atom property)
{
    Atom qvdRedirect = MakeAtom(QVD_REDIRECT_XPROP, strlen(QVD_REDIRECT_XPROP), True);
    if (property == qvdRedirect)
      {

        Window remote = nxagentWindowPriv(pWin)->window;
	_delRedirectWindow(remote);
#ifdef DEBUG
	fprintf(stderr, "Enabling window 0x%x to have direct window access, bypassing NX input window\n",
		(unsigned int)remote);
#endif

      }

  return 0;
}
