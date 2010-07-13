#!/usr/bin/env python
"""This launches an echoing rep socket device,
and runs a blocking numpy action. The rep socket should
remain responsive to pings during this time."""
import time
import numpy
import zmq

ctx = zmq.Context()

# rep = ctx.socket(zmq.REP)
# rep.bind('tcp://127.0.0.1:10111')


dev = zmq.ThreadsafeDevice(zmq.FORWARDER, zmq.REP, -1)
print "b"
dev.bind_in('tcp://127.0.0.1:10111')
dev.setsockopt_in(zmq.IDENTITY, "whoda")
dev.start()
print "c"
#wait for connections
time.sleep(1)

A = numpy.random.random((2**11,2**12))
print "starting blocking loop"
while True:
    tic = time.time()
    numpy.dot(A,A.transpose())
    print "blocked for %.3f s"%(time.time()-tic)

