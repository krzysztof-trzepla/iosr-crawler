#!/usr/bin/env bash

riak-admin bucket-type create set '{"n_val":3, "props":{"datatype":"set"}}'
riak-admin bucket-type activate set
