def new(num_buckets=256):
    """Initializes a Map with a given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap
  
def hash_key(aMap, key):
    """Given a key, this will create a number and convert it to an index for the aMap's buckets."""
    print hash(key), len(aMap), hash(key) % len(aMap)
    return hash(key) % len(aMap)
  
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
    
def get_slot(aMap, key, default=None):
    """Returns the index, key, and value of a slot found in a bucket."""
    bucket = get_bucket(aMap, key)
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    
    return -1, key, default
    
def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v
    
def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    
    if v:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))
        
def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break
            
def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v
                
jazz = new()
set(jazz, 'Miles Davis', 'Flamenco Sketches')
# confirms set will replace previous one
set(jazz, 'Miles Davis', 'Kind Of Blue')
set(jazz, 'Duke Ellington', 'Beginning To See The Light')
set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- List Test ----"
list(jazz)

print "---- Get Test ----"
print get(jazz, 'Miles Davis')
print get(jazz, 'Duke Ellington')
print get(jazz, 'Billy Strayhorn')

print "---- Delete Test ----"
print "** Goodbye Miles"
delete(jazz, "Miles Davis")
list(jazz)

delete(jazz, "Duke Ellington")
list(jazz)

delete(jazz, "Billy Strayhorn")
list(jazz)

print "** Goodbye Pork Pie Hat"
delete (jazz, "Charles Mingus") 