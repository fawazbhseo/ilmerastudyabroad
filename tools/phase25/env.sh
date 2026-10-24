#!/bin/sh
# Install dependencies outside the checkout. No runtime output is deployable.
export NODE_PATH="${PHASE25_RUNTIME:-/home/user/phase25-runtime}/node_modules"
export PATH="${PHASE25_RUNTIME:-/home/user/phase25-runtime}/bin:$PATH"
export LD_LIBRARY_PATH="${PHASE25_RUNTIME:-/home/user/phase25-runtime}/libs/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export PYTHONPATH="${PHASE25_RUNTIME:-/home/user/phase25-runtime}/pylibs${PYTHONPATH:+:$PYTHONPATH}"
