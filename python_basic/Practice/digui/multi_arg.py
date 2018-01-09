#encoding=utf8
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head
if __name__ == '__main__':
	items = [1, 10, 7, 4, 5, 9]
	sum(items)
