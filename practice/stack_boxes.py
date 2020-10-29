import collections

Box = collections.namedtuple('Box', ['height', 'width', 'depth'])

def can_be_above(below, above):
    if below is None:
        return True
    if below.height > above.height and below.width > above.width and below.depth > above.depth:
        return True
    return False

def get_max_box_height(boxes, idx, last_taken):
    if idx >= len(boxes):
        return 0
    h1 = 0
    if can_be_above(last_taken, boxes[idx]):
        h1 = get_max_box_height(boxes, idx + 1, boxes[idx])
        h1 += boxes[idx].height
    h2 = get_max_box_height(boxes, idx + 1, last_taken)
    max_height = max(h1, h2)
    return max_height

def sort_height(box):
    return box.height

def main():
    boxes = [
        Box(1, 2, 3),
        Box(4, 5, 6),
        Box(6, 5, 4),
    ]
    boxes = sorted(boxes, key=sort_height, reverse=True)
    print(boxes)

    max_height = get_max_box_height(boxes, 0, None)
    print(max_height)

main()
