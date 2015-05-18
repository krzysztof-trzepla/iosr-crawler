#!/usr/bin/env bash

../riak-2.0.5/bin/riak start
../riak-2.0.5/bin/riak-admin bucket-type create set '{"n_val":3, "props":{"datatype":"set"}}'
../riak-2.0.5/bin/riak-admin bucket-type activate set
../riak-2.0.5/bin/riak-admin bucket-type create counter '{"n_val":3, "props":{"datatype":"counter"}}'
../riak-2.0.5/bin/riak-admin bucket-type activate counter
