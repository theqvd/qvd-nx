/**************************************************************************/
/*                                                                        */
/*                                                                        */
/* redirect events to local windows from NX windows                       */
/*                                                                        */
/*                                                                        */
/*                                                                        */
/*                                                                        */
/*                                                                        */
/**************************************************************************/

#ifndef __NXLOCALEVENTS_H__
#define __NXLOCALEVENTS_H__

#define QVD_REDIRECT_XPROP "_QVD_REDIRECT_EVENT"

int DeliverLocalEventsToQvdWindow(WindowPtr pWin, xEvent *pEvents);
int ChangeWindowPropertyQvdRedirectEvent(WindowPtr pWin, Atom property);
int DeleteWindowPropertyQvdRedirectEvent(WindowPtr pWin, Atom property);

#endif /* __NXLOCALEVENTS_H__ */
