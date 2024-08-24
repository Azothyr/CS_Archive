class HashMap:
    def __init__(self, initial_capacity=7):
        self.buckets = [None] * initial_capacity
        self.num_entries = 0

    def get(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            raise KeyError(f'Key {key} not found')
        else:
            for k, v in self.buckets[index]:
                if k == key:
                    return v
            raise KeyError(f'Key {key} not found')

    def set(self, key, value):
        if self.load_factor() >= 0.8:
            self._rehash()
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = [(key, value)]
        else:
            for i, kv in enumerate(self.buckets[index]):
                if kv[0] == key:
                    self.buckets[index][i] = (key, value)
                    return
            self.buckets[index].append((key, value))
        self.num_entries += 1

    def remove(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            return
        for i, kv in enumerate(self.buckets[index]):
            if kv[0] == key:
                del self.buckets[index][i]
                self.num_entries -= 1
                return

    def clear(self):
        self.buckets = [None] * len(self.buckets)
        self.num_entries = 0

    def capacity(self):
        return len(self.buckets)

    def size(self):
        return self.num_entries

    def keys(self):
        result = []
        for bucket in self.buckets:
            if bucket is not None:
                result.extend(k for k, v in bucket)
        return result

    def load_factor(self):
        return self.num_entries / self.capacity()

    def _hash(self, key):
        r, c = key
        return ((r * r + r) // 2 + c) % self.capacity()

    def _rehash(self):
        old_buckets = self.buckets
        self.buckets = [None] * (self.capacity() * 2 - 1)
        self.num_entries = 0
        for bucket in old_buckets:
            if bucket is not None:
                for k, v in bucket:
                    self.set(k, v)
