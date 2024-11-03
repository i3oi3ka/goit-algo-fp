# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.


class Node:
    def __init__(self, data: int = None):
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол


class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку пустий

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = (
            self.head
        )  # Вказує, що новий вузол має посилатися на поточний головний вузол
        self.head = new_node  # Робить новий вузол головним вузлом списку

    def insert_at_end(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        if self.head is None:  # Якщо список пустий
            self.head = new_node  # Робить новий вузол головним вузлом
        else:
            cur = self.head  # Починає з головного вузла
            while cur.next:  # Проходить до кінця списку
                cur = cur.next
            cur.next = new_node  # Додає новий вузол в кінці списку

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:  # Перевіряє, чи існує попередній вузол
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = (
            prev_node.next
        )  # Вказує, що новий вузол має посилатися на вузол після попереднього вузла
        prev_node.next = new_node  # Вставляє новий вузол після попереднього вузла

    def delete_node(self, key: int):
        cur = self.head  # Починає з головного вузла
        if cur and cur.data == key:  # Якщо головний вузол містить потрібні дані
            self.head = cur.next  # Робить наступний вузол головним
            cur = None  # Видаляє вузол
            return
        prev = None  # Змінна для зберігання попереднього вузла
        while cur and cur.data != key:  # Проходить список у пошуках потрібних даних
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо вузол з потрібними даними не знайдено
            return
        prev.next = cur.next  # Видаляє вузол з потрібними даними
        cur = None  # Звільняє пам'ять, видаляючи вузол

    def search_element(self, data: int) -> Node | None:
        cur = self.head  # Починає з головного вузла
        while cur:  # Проходить список у пошуках потрібних даних
            if cur.data == data:  # Якщо знайдено потрібні дані
                return cur  # Повертає вузол з потрібними даними
            cur = cur.next
        return None  # Якщо вузол з потрібними даними не знайдено

    def print_list(self):
        current = self.head  # Починає з головного вузла
        while current:  # Проходить весь список
            print(current.data, end=" -> ")  # Виводить дані вузла
            current = current.next  # Переходить до наступного вузла
        print("None")  # Вказує на кінець списку

    def reverse(self):
        if self.head:
            next = self.head.next
            self.head.next = None
            curr = self.head
            while next:
                temp = next.next
                next.next = curr
                curr = next
                next = temp
            self.head = curr

    def merge_list(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError
        curr = self.head
        other_curr = other.head
        temp = self.head
        while curr and other_curr:
            if not curr.next:
                temp = curr
            if curr.data <= other_curr.data:
                curr = curr.next
            else:
                new_node = Node(curr.data)
                new_node.next = curr.next
                curr.next = new_node
                curr.data = other_curr.data
                curr = curr.next
                other_curr = other_curr.next

        while other_curr:
            if not temp:
                self.head = Node(other_curr.data)
                temp = self.head
            else:
                temp.next = Node(other_curr.data)
                temp = temp.next
            other_curr = other_curr.next

    def merge_sort(self):
        if not self.head or not self.head.next:
            return
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        if not head or not head.next:
            return head

        # Знаходимо середину списку
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Розділяємо список на дві частини

        # Рекурсивно сортуємо кожну половину
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        # Об'єднуємо відсортовані частини
        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        # Об'єднуємо два відсортовані підсписки
        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)
        return result


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(100)
    llist.insert_at_beginning(-10)
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(30)
    llist.insert_at_beginning(12)
    llist.print_list()
    llist.reverse()
    llist.print_list()

    llist1 = LinkedList()
    llist1.insert_at_beginning(17)
    llist1.insert_at_beginning(10)
    llist1.reverse()
    llist1.print_list()
    llist1.insert_at_beginning(17)
    llist1.insert_at_beginning(10)
    llist1.insert_at_beginning(5)
    llist1.insert_at_beginning(5)
    llist1.insert_at_beginning(3)

    llist2 = LinkedList()
    llist2.insert_at_beginning(25)
    llist2.insert_at_beginning(20)
    llist2.insert_at_beginning(15)
    llist2.insert_at_beginning(12)
    llist2.insert_at_beginning(2)
    llist2.insert_at_beginning(2)

    llist1.print_list()
    llist2.print_list()

    llist3 = LinkedList()
    llist1.merge_list(llist2)
    llist1.print_list()

    llist.merge_sort()
    llist.print_list()
