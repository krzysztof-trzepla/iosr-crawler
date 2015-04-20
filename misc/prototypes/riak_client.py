import riak

myClient = riak.RiakClient(pb_port=8087, protocol='pbc')

myBucket = myClient.bucket('test')

val1 = 1
key1 = myBucket.new('one', data=val1)
key1.store()

fetched1 = myBucket.get('one')

print fetched1.data