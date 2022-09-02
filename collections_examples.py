# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaabbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0])
print(list(my_counter.elements()))

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
ordered_dict['d'] = 4
print(ordered_dict)

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])
print(d)

dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.clear()
print(dq)
dq.extend([4, 5, 6])
print(dq)
dq.extendleft([2, 3])
print(dq)
dq.rotate(1)
print(dq)
dq.rotate(-1)
print(dq)
