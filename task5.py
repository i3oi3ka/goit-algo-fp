from task4 import draw_tree, Node, build_heap_tree


def count_nodes(node: Node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def generate_color(step, count_node):
    base_color = [0, 0, 255]
    white = [255, 255, 255]
    ratio = step / count_node
    color = [int(base + ratio * (w - base)) for base, w in zip(base_color, white)]
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def dfs_visualize(node: Node, count_node: int):
    stack = [node]
    step = 0
    while stack:
        node = stack.pop()
        node.color = generate_color(step, count_node)
        step += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def bfs_visualize(node: Node, count_node: int):
    queue = [node]
    step = 0
    while queue:
        node = queue.pop()
        node.color = generate_color(step, count_node)
        step += 1
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

total_steps = count_nodes(root)

dfs_visualize(root, total_steps)
draw_tree(root)

bfs_visualize(root, total_steps)
draw_tree(root)
