from task4 import draw_tree, Node
import  heapq


def count_nodes(node: Node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def generate_color(step, total_steps):
    base_color = [135, 206, 250]
    white = [255, 255, 255]
    ratio = step / total_steps
    color = [int(base + ratio * (w - base)) for base, w in zip(base_color, white)]
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def dfs_visualize(root: Node, total_steps: int):
    stack = [root]
    step = 0
    while stack:
        root = stack.pop()
        root.color = generate_color(step, total_steps)
        step += 1
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


def bfs_visualize(root: Node, total_steps: int):
    queue = [root]
    step = 0
    while queue:
        root = queue.pop()
        root.color = generate_color(step, total_steps)
        step += 1
        if root.left:
            queue.insert(0, root.left)
        if root.right:
            queue.insert(0, root.right)


heap_list = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap_list)

print(heap_list)
heap_tree_root = build_heap_tree(heap_list, None, 0, len(heap_list))

total_steps = count_nodes(root)

dfs_visualize(root, total_steps)
draw_tree(root)

bfs_visualize(root, total_steps)
draw_tree(root)
