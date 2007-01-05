#!/bin/sh

RRDTOOL=/usr/bin/rrdtool
OUTDIR=/var/lib/lighttpd/rrd
INFILE=/var/lib/lighttpd/lighttpd.rrd
OUTPRE=lighttpd-traffic

exec >/dev/null

DISP="DEF:bin=$INFILE:InOctets:AVERAGE \
      DEF:bout=$INFILE:OutOctets:AVERAGE \
      LINE1:bin#0000FF:in \
      LINE1:bout#FF0000:out \
      -v bytes/s"

$RRDTOOL graph $OUTDIR/$OUTPRE-hour.png -a PNG --start -14400 $DISP
$RRDTOOL graph $OUTDIR/$OUTPRE-day.png -a PNG --start -86400 $DISP
$RRDTOOL graph $OUTDIR/$OUTPRE-month.png -a PNG --start -2592000 $DISP

OUTPRE=lighttpd-requests

DISP="DEF:req=$INFILE:Requests:AVERAGE \
      LINE1:req#0000FF:requests \
      -v req/s"

$RRDTOOL graph $OUTDIR/$OUTPRE-hour.png -a PNG --start -14400 $DISP
$RRDTOOL graph $OUTDIR/$OUTPRE-day.png -a PNG --start -86400 $DISP
$RRDTOOL graph $OUTDIR/$OUTPRE-month.png -a PNG --start -2592000 $DISP
