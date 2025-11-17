"""
Queue Data Structure Implementation

A comprehensive implementation of a Queue data structure with:
- enqueue(): Add element to rear of queue
- dequeue(): Remove element from front of queue
- is_empty(): Check if queue is empty

Also includes:
- peek(): View front element without removing
- size(): Get number of elements
- display(): Show all elements
- clear(): Remove all elements
- Interactive menu system

Queue is a First-In-First-Out (FIFO) data structure where elements
are added at the rear and removed from the front.
"""

import logging
from typing import Any, Optional, List
from collections import deque
from enum import Enum
import time


# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class QueueError(Exception):
    """Base exception for queue operations."""
    pass


class QueueUnderflowError(QueueError):
    """Raised when trying to dequeue from empty queue."""
    pass


class QueueOverflowError(QueueError):
    """Raised when queue exceeds maximum capacity."""
    pass


class QueueEmptyError(QueueError):
    """Raised when peek is called on empty queue."""
    pass


# ============================================================================
# QUEUE IMPLEMENTATION V1: BASIC QUEUE (LIST-BASED)
# ============================================================================

class Queue:
    """
    Basic Queue implementation using Python list.
    
    A queue is a First-In-First-Out (FIFO) data structure where
    elements are added at the rear and removed from the front.
    
    Attributes
    ----------
    items : list
        Internal list to store queue elements.
    
    Methods
    -------
    enqueue(item)
        Add item to rear of queue.
    dequeue()
        Remove and return front item.
    peek()
        View front item without removing.
    is_empty()
        Check if queue is empty.
    size()
        Get number of elements.
    display()
        Show all elements.
    clear()
        Remove all elements.
    
    Examples
    --------
    >>> queue = Queue()
    >>> queue.enqueue(1)
    >>> queue.enqueue(2)
    >>> queue.enqueue(3)
    >>> queue.dequeue()
    1
    >>> queue.peek()
    2
    >>> queue.is_empty()
    False
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items: List[Any] = []
        logger.info("✓ Queue created successfully")
    
    def enqueue(self, item: Any) -> None:
        """
        Add item to rear of queue.
        
        Parameters
        ----------
        item : Any
            Item to add to queue.
        
        Returns
        -------
        None
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> queue = Queue()
        >>> queue.enqueue(10)
        >>> queue.enqueue(20)
        """
        self.items.append(item)
        logger.info(f"✓ Enqueued: {item} (Queue size: {len(self.items)})")
    
    def dequeue(self) -> Any:
        """
        Remove and return front item from queue.
        
        Returns
        -------
        Any
            Item removed from front of queue.
        
        Raises
        ------
        QueueUnderflowError
            If queue is empty.
        
        Time Complexity: O(n) - because list.pop(0) is O(n)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> queue = Queue()
        >>> queue.enqueue(10)
        >>> queue.dequeue()
        10
        """
        if self.is_empty():
            error_msg = "Cannot dequeue from empty queue"
            logger.error(f"✗ {error_msg}")
            raise QueueUnderflowError(error_msg)
        
        item = self.items.pop(0)
        logger.info(f"✓ Dequeued: {item} (Queue size: {len(self.items)})")
        return item
    
    def peek(self) -> Any:
        """
        View front item without removing it.
        
        Returns
        -------
        Any
            Item at front of queue.
        
        Raises
        ------
        QueueEmptyError
            If queue is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> queue = Queue()
        >>> queue.enqueue(10)
        >>> queue.peek()
        10
        """
        if self.is_empty():
            error_msg = "Queue is empty, cannot peek"
            logger.error(f"✗ {error_msg}")
            raise QueueEmptyError(error_msg)
        
        logger.info(f"✓ Peeked: {self.items[0]}")
        return self.items[0]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns
        -------
        bool
            True if queue is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Examples
        --------
        >>> queue = Queue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue(10)
        >>> queue.is_empty()
        False
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get number of elements in queue.
        
        Returns
        -------
        int
            Number of elements.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items)
    
    def display(self) -> None:
        """
        Display all elements in queue from front to rear.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty():
            print("  Queue is empty")
            return
        
        print("  Queue (front to rear):")
        for i, item in enumerate(self.items):
            marker = " <- FRONT" if i == 0 else ""
            marker += " <- REAR" if i == len(self.items) - 1 else ""
            print(f"    [{i}] {item}{marker}")
    
    def clear(self) -> None:
        """
        Remove all elements from queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.items.clear()
        logger.info("✓ Queue cleared")
    
    def __str__(self) -> str:
        """String representation of queue."""
        if self.is_empty():
            return "Queue: []"
        return f"Queue: {self.items} (size: {len(self.items)})"
    
    def __repr__(self) -> str:
        """Detailed representation of queue."""
        return f"Queue({self.items})"


# ============================================================================
# QUEUE IMPLEMENTATION V2: OPTIMIZED USING DEQUE
# ============================================================================

class OptimizedQueue:
    """
    Optimized Queue implementation using collections.deque.
    
    Benefits over list-based:
    - O(1) dequeue operation (vs O(n) with list.pop(0))
    - More efficient for large queues
    - Better performance for producer-consumer patterns
    
    Attributes
    ----------
    items : deque
        Internal deque to store queue elements.
    """
    
    def __init__(self):
        """Initialize an empty optimized queue."""
        self.items: deque = deque()
        logger.info("✓ Optimized Queue created successfully")
    
    def enqueue(self, item: Any) -> None:
        """
        Add item to rear of queue.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.items.append(item)
        logger.info(f"✓ Enqueued: {item} (Queue size: {len(self.items)})")
    
    def dequeue(self) -> Any:
        """
        Remove and return front item from queue.
        
        Time Complexity: O(1) - Much better than list version!
        Space Complexity: O(1)
        
        Raises
        ------
        QueueUnderflowError
            If queue is empty.
        """
        if self.is_empty():
            error_msg = "Cannot dequeue from empty queue"
            logger.error(f"✗ {error_msg}")
            raise QueueUnderflowError(error_msg)
        
        item = self.items.popleft()
        logger.info(f"✓ Dequeued: {item} (Queue size: {len(self.items)})")
        return item
    
    def peek(self) -> Any:
        """
        View front item without removing it.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.is_empty():
            error_msg = "Queue is empty, cannot peek"
            logger.error(f"✗ {error_msg}")
            raise QueueEmptyError(error_msg)
        
        logger.info(f"✓ Peeked: {self.items[0]}")
        return self.items[0]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get number of elements in queue."""
        return len(self.items)
    
    def display(self) -> None:
        """Display all elements in queue."""
        if self.is_empty():
            print("  Queue is empty")
            return
        
        print("  Queue (front to rear):")
        for i, item in enumerate(self.items):
            marker = " <- FRONT" if i == 0 else ""
            marker += " <- REAR" if i == len(self.items) - 1 else ""
            print(f"    [{i}] {item}{marker}")
    
    def clear(self) -> None:
        """Remove all elements from queue."""
        self.items.clear()
        logger.info("✓ Queue cleared")


# ============================================================================
# QUEUE IMPLEMENTATION V3: BOUNDED QUEUE
# ============================================================================

class BoundedQueue(Queue):
    """
    Queue with maximum capacity limit.
    
    Parameters
    ----------
    max_size : int
        Maximum number of elements allowed.
    """
    
    def __init__(self, max_size: int = 100):
        """Initialize bounded queue."""
        super().__init__()
        self.max_size = max_size
        logger.info(f"✓ Bounded Queue created (max_size: {max_size})")
    
    def enqueue(self, item: Any) -> None:
        """
        Add item to queue with overflow check.
        
        Raises
        ------
        QueueOverflowError
            If queue is full.
        """
        if len(self.items) >= self.max_size:
            error_msg = f"Queue overflow: Maximum size {self.max_size} reached"
            logger.error(f"✗ {error_msg}")
            raise QueueOverflowError(error_msg)
        
        super().enqueue(item)
    
    def is_full(self) -> bool:
        """Check if queue is at maximum capacity."""
        return len(self.items) == self.max_size


# ============================================================================
# QUEUE IMPLEMENTATION V4: TYPED QUEUE
# ============================================================================

class TypedQueue(Queue):
    """
    Queue that enforces a specific data type.
    
    Parameters
    ----------
    allowed_type : type
        Type of items allowed in queue.
    """
    
    def __init__(self, allowed_type: type = int):
        """Initialize typed queue."""
        super().__init__()
        self.allowed_type = allowed_type
        logger.info(f"✓ Typed Queue created (type: {allowed_type.__name__})")
    
    def enqueue(self, item: Any) -> None:
        """
        Add item to queue with type check.
        
        Raises
        ------
        TypeError
            If item is not of allowed type.
        """
        if not isinstance(item, self.allowed_type):
            error_msg = (
                f"Type error: Expected {self.allowed_type.__name__}, "
                f"got {type(item).__name__}"
            )
            logger.error(f"✗ {error_msg}")
            raise TypeError(error_msg)
        
        super().enqueue(item)


# ============================================================================
# QUEUE IMPLEMENTATION V5: PRIORITY QUEUE
# ============================================================================

class PriorityQueue:
    """
    Priority Queue implementation.
    
    Elements are dequeued based on priority (lower number = higher priority).
    """
    
    def __init__(self):
        """Initialize empty priority queue."""
        self.items: List[tuple] = []
        logger.info("✓ Priority Queue created successfully")
    
    def enqueue(self, item: Any, priority: int = 0) -> None:
        """
        Add item with priority to queue.
        
        Parameters
        ----------
        item : Any
            Item to add.
        priority : int
            Priority level (lower = higher priority, default 0)
        """
        self.items.append((priority, item))
        # Sort by priority
        self.items.sort(key=lambda x: x[0])
        logger.info(f"✓ Enqueued: {item} (priority: {priority})")
    
    def dequeue(self) -> Any:
        """Remove and return highest priority item."""
        if self.is_empty():
            error_msg = "Cannot dequeue from empty queue"
            logger.error(f"✗ {error_msg}")
            raise QueueUnderflowError(error_msg)
        
        priority, item = self.items.pop(0)
        logger.info(f"✓ Dequeued: {item} (priority: {priority})")
        return item
    
    def peek(self) -> Any:
        """View highest priority item."""
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")
        return self.items[0][1]
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get number of elements."""
        return len(self.items)
    
    def display(self) -> None:
        """Display all elements with priorities."""
        if self.is_empty():
            print("  Priority Queue is empty")
            return
        
        print("  Priority Queue (front to rear):")
        for i, (priority, item) in enumerate(self.items):
            marker = " <- HIGHEST PRIORITY" if i == 0 else ""
            print(f"    [{i}] {item} (priority: {priority}){marker}")
    
    def clear(self) -> None:
        """Remove all elements."""
        self.items.clear()
        logger.info("✓ Priority Queue cleared")


# ============================================================================
# QUEUE IMPLEMENTATION V6: LINKED LIST BASED
# ============================================================================

class Node:
    """Node for linked list implementation."""
    
    def __init__(self, data: Any):
        """Initialize node."""
        self.data = data
        self.next = None


class LinkedListQueue:
    """
    Queue implementation using linked list.
    
    Benefits:
    - Dynamic size (no overflow)
    - O(1) enqueue and dequeue
    - Better for variable-sized data
    """
    
    def __init__(self):
        """Initialize empty linked list queue."""
        self.front = None
        self.rear = None
        self._size = 0
        logger.info("✓ Linked List Queue created")
    
    def enqueue(self, item: Any) -> None:
        """Add item to rear of queue."""
        new_node = Node(item)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
        logger.info(f"✓ Enqueued: {item} (Queue size: {self._size})")
    
    def dequeue(self) -> Any:
        """Remove and return front item."""
        if self.is_empty():
            error_msg = "Cannot dequeue from empty queue"
            logger.error(f"✗ {error_msg}")
            raise QueueUnderflowError(error_msg)
        
        item = self.front.data
        self.front = self.front.next
        self._size -= 1
        
        if self.is_empty():
            self.rear = None
        
        logger.info(f"✓ Dequeued: {item} (Queue size: {self._size})")
        return item
    
    def peek(self) -> Any:
        """View front item."""
        if self.is_empty():
            error_msg = "Queue is empty, cannot peek"
            logger.error(f"✗ {error_msg}")
            raise QueueEmptyError(error_msg)
        
        logger.info(f"✓ Peeked: {self.front.data}")
        return self.front.data
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self.front is None
    
    def size(self) -> int:
        """Get number of elements."""
        return self._size
    
    def display(self) -> None:
        """Display all elements."""
        if self.is_empty():
            print("  Queue is empty")
            return
        
        print("  Queue (front to rear):")
        current = self.front
        index = 0
        while current:
            marker = " <- FRONT" if index == 0 else ""
            if current == self.rear:
                marker += " <- REAR"
            print(f"    [{index}] {current.data}{marker}")
            current = current.next
            index += 1
    
    def clear(self) -> None:
        """Remove all elements."""
        self.front = self.rear = None
        self._size = 0
        logger.info("✓ Queue cleared")


# ============================================================================
# INTERACTIVE MENU SYSTEM
# ============================================================================

class QueueMenu:
    """Interactive menu system for queue operations."""
    
    def __init__(self, queue_type: str = "basic"):
        """
        Initialize menu with specified queue type.
        
        Parameters
        ----------
        queue_type : str
            Type of queue: "basic", "optimized", "bounded", 
            "typed", "priority", "linkedlist"
        """
        self.queue_type = queue_type
        self.queue = self._create_queue(queue_type)
        logger.info(f"✓ Menu created with {queue_type} queue")
    
    def _create_queue(self, queue_type: str):
        """Create queue of specified type."""
        if queue_type == "basic":
            return Queue()
        elif queue_type == "optimized":
            return OptimizedQueue()
        elif queue_type == "bounded":
            return BoundedQueue(max_size=10)
        elif queue_type == "typed":
            return TypedQueue(allowed_type=int)
        elif queue_type == "priority":
            return PriorityQueue()
        elif queue_type == "linkedlist":
            return LinkedListQueue()
        else:
            return Queue()
    
    def display_menu(self):
        """Display main menu options."""
        print("\n" + "="*60)
        print("QUEUE OPERATIONS MENU")
        print("="*60)
        print("1. Enqueue - Add element to queue")
        print("2. Dequeue - Remove element from queue")
        print("3. Peek - View front element")
        print("4. Display - Show all elements")
        print("5. Size - Get number of elements")
        print("6. Is Empty - Check if queue is empty")
        print("7. Clear - Remove all elements")
        
        if isinstance(self.queue, BoundedQueue):
            print("8. Is Full - Check if queue is full")
        
        if isinstance(self.queue, PriorityQueue):
            print("8. Enqueue with Priority")
        
        print("0. Exit - Quit program")
        print("="*60)
    
    def run(self):
        """Run interactive menu system."""
        print("\n" + "="*60)
        print(f"QUEUE IMPLEMENTATION - {self.queue_type.upper()}")
        print("="*60)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-8): ").strip()
            
            try:
                if choice == "1":
                    self._handle_enqueue()
                elif choice == "2":
                    self._handle_dequeue()
                elif choice == "3":
                    self._handle_peek()
                elif choice == "4":
                    self._handle_display()
                elif choice == "5":
                    self._handle_size()
                elif choice == "6":
                    self._handle_is_empty()
                elif choice == "7":
                    self._handle_clear()
                elif choice == "8":
                    if isinstance(self.queue, BoundedQueue):
                        self._handle_is_full()
                    elif isinstance(self.queue, PriorityQueue):
                        self._handle_priority_enqueue()
                elif choice == "0":
                    print("\n✓ Thank you for using Queue Implementation!")
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
            
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
    
    def _handle_enqueue(self):
        """Handle enqueue operation."""
        try:
            if isinstance(self.queue, TypedQueue):
                value = int(input("Enter integer value: "))
            else:
                value = input("Enter value: ")
            
            self.queue.enqueue(value)
            print(f"✓ Successfully enqueued: {value}")
        except ValueError:
            print("❌ Invalid input. Please enter a number for integer queue.")
        except QueueOverflowError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_priority_enqueue(self):
        """Handle priority enqueue operation."""
        try:
            value = input("Enter value: ")
            priority = int(input("Enter priority (lower = higher): "))
            
            if isinstance(self.queue, PriorityQueue):
                self.queue.enqueue(value, priority)
                print(f"✓ Successfully enqueued: {value} (priority: {priority})")
        except ValueError:
            print("❌ Invalid input. Priority must be a number.")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_dequeue(self):
        """Handle dequeue operation."""
        try:
            item = self.queue.dequeue()
            print(f"✓ Successfully dequeued: {item}")
        except QueueUnderflowError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_peek(self):
        """Handle peek operation."""
        try:
            item = self.queue.peek()
            print(f"✓ Front element: {item}")
        except QueueEmptyError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_display(self):
        """Handle display operation."""
        print("\n" + "-"*40)
        self.queue.display()
        print("-"*40)
    
    def _handle_size(self):
        """Handle size operation."""
        size = self.queue.size()
        print(f"✓ Queue size: {size} elements")
    
    def _handle_is_empty(self):
        """Handle is_empty operation."""
        is_empty = self.queue.is_empty()
        status = "empty" if is_empty else "not empty"
        print(f"✓ Queue is {status}")
    
    def _handle_clear(self):
        """Handle clear operation."""
        self.queue.clear()
        print("✓ Queue cleared successfully")
    
    def _handle_is_full(self):
        """Handle is_full operation."""
        if isinstance(self.queue, BoundedQueue):
            is_full = self.queue.is_full()
            status = "full" if is_full else "not full"
            print(f"✓ Queue is {status} (capacity: {self.queue.max_size})")


# ============================================================================
# DEMONSTRATIONS AND TESTS
# ============================================================================

def demonstrate_basic_queue():
    """Demonstrate basic queue operations."""
    print("="*80)
    print("DEMONSTRATION 1: Basic Queue Operations")
    print("="*80)
    
    queue = Queue()
    
    print("\n1. Checking if queue is empty:")
    print(f"   is_empty(): {queue.is_empty()}")
    
    print("\n2. Enqueueing elements: 10, 20, 30, 40, 50")
    for value in [10, 20, 30, 40, 50]:
        queue.enqueue(value)
    
    print("\n3. Queue status:")
    print(f"   Size: {queue.size()}")
    print(f"   Is empty: {queue.is_empty()}")
    
    print("\n4. Displaying queue:")
    queue.display()
    
    print("\n5. Peeking at front:")
    front = queue.peek()
    print(f"   Front element: {front}")
    
    print("\n6. Dequeueing elements:")
    for i in range(3):
        item = queue.dequeue()
        print(f"   Dequeued: {item}")
    
    print("\n7. Queue after 3 dequeues:")
    queue.display()
    
    print("\n8. Dequeueing remaining elements:")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"   Dequeued: {item}")
    
    print("\n9. Final state:")
    print(f"   Size: {queue.size()}")
    print(f"   Is empty: {queue.is_empty()}")


def demonstrate_optimized_queue():
    """Demonstrate optimized queue."""
    print("\n" + "="*80)
    print("DEMONSTRATION 2: Optimized Queue (Using Deque)")
    print("="*80)
    
    queue = OptimizedQueue()
    
    print("\n1. Enqueueing 100 elements:")
    for i in range(1, 101):
        queue.enqueue(i * 10)
    
    print(f"   ✓ Enqueued 100 elements")
    print(f"   Queue size: {queue.size()}")
    
    print("\n2. Dequeueing first 5 elements:")
    for i in range(5):
        item = queue.dequeue()
        print(f"   [{i+1}] Dequeued: {item}")
    
    print(f"\n3. Queue size after dequeues: {queue.size()}")


def demonstrate_bounded_queue():
    """Demonstrate bounded queue."""
    print("\n" + "="*80)
    print("DEMONSTRATION 3: Bounded Queue (max size: 5)")
    print("="*80)
    
    queue = BoundedQueue(max_size=5)
    
    print("\n1. Enqueueing 5 elements:")
    for i in range(1, 6):
        queue.enqueue(i * 100)
        print(f"   Enqueued: {i*100}, Is full: {queue.is_full()}")
    
    print("\n2. Attempting to enqueue when full:")
    try:
        queue.enqueue(600)
    except QueueOverflowError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n3. Queue display:")
    queue.display()


def demonstrate_typed_queue():
    """Demonstrate typed queue."""
    print("\n" + "="*80)
    print("DEMONSTRATION 4: Typed Queue (integers only)")
    print("="*80)
    
    queue = TypedQueue(allowed_type=int)
    
    print("\n1. Enqueueing valid integers:")
    for value in [100, 200, 300]:
        queue.enqueue(value)
        print(f"   Enqueued: {value}")
    
    print("\n2. Attempting to enqueue string:")
    try:
        queue.enqueue("invalid")
    except TypeError as e:
        print(f"   ✓ Caught: {e}")
    
    print("\n3. Queue display:")
    queue.display()


def demonstrate_priority_queue():
    """Demonstrate priority queue."""
    print("\n" + "="*80)
    print("DEMONSTRATION 5: Priority Queue")
    print("="*80)
    
    pq = PriorityQueue()
    
    print("\n1. Enqueueing with priorities:")
    items = [
        ("Emergency", 1),
        ("Normal", 5),
        ("Low", 10),
        ("High", 2),
        ("Medium", 7)
    ]
    
    for item, priority in items:
        pq.enqueue(item, priority)
        print(f"   Enqueued: {item} (priority: {priority})")
    
    print("\n2. Queue display (sorted by priority):")
    pq.display()
    
    print("\n3. Dequeueing in priority order:")
    while not pq.is_empty():
        item = pq.dequeue()
        print(f"   Dequeued: {item}")


def demonstrate_linked_list_queue():
    """Demonstrate linked list queue."""
    print("\n" + "="*80)
    print("DEMONSTRATION 6: Linked List Queue")
    print("="*80)
    
    queue = LinkedListQueue()
    
    print("\n1. Enqueueing elements: A, B, C, D, E")
    for value in ['A', 'B', 'C', 'D', 'E']:
        queue.enqueue(value)
    
    print("\n2. Queue display:")
    queue.display()
    
    print("\n3. Peeking and dequeueing:")
    print(f"   Peek: {queue.peek()}")
    print(f"   Dequeue: {queue.dequeue()}")
    print(f"   Dequeue: {queue.dequeue()}")
    
    print("\n4. Queue after operations:")
    queue.display()


def demonstrate_producer_consumer():
    """Demonstrate producer-consumer pattern."""
    print("\n" + "="*80)
    print("DEMONSTRATION 7: Producer-Consumer Pattern")
    print("="*80)
    
    queue = OptimizedQueue()
    
    print("\n1. Producer produces 5 items:")
    for i in range(1, 6):
        item = f"Item-{i}"
        queue.enqueue(item)
        print(f"   Produced: {item}")
    
    print(f"\n2. Queue status: {queue.size()} items waiting")
    
    print("\n3. Consumer consumes 3 items:")
    for i in range(3):
        item = queue.dequeue()
        print(f"   Consumed: {item}")
    
    print(f"\n4. Queue status: {queue.size()} items remaining")


def show_use_cases():
    """Show real-world use cases."""
    print("\n" + "="*80)
    print("REAL-WORLD USE CASES OF QUEUES")
    print("="*80)
    
    use_cases = [
        {
            "name": "Printer Queue",
            "description": "Print jobs waiting to be processed",
            "example": "Documents enqueued, printed in order (FIFO)"
        },
        {
            "name": "Customer Service",
            "description": "Customers waiting for service",
            "example": "Customers enqueued, served in order"
        },
        {
            "name": "Network Packets",
            "description": "Data packets in network buffers",
            "example": "Packets enqueued at router, forwarded FIFO"
        },
        {
            "name": "Job Scheduling",
            "description": "Tasks in operating system scheduler",
            "example": "Processes enqueued, executed in order"
        },
        {
            "name": "BFS Algorithm",
            "description": "Breadth-first search traversal",
            "example": "Nodes enqueued level by level"
        },
        {
            "name": "Message Queue",
            "description": "Asynchronous message passing",
            "example": "Messages enqueued, processed by consumers"
        },
        {
            "name": "Call Center",
            "description": "Incoming calls holding",
            "example": "Calls enqueued, answered by agents"
        },
        {
            "name": "Cache Management",
            "description": "LRU cache eviction",
            "example": "Items enqueued, least recently used removed"
        }
    ]
    
    for i, case in enumerate(use_cases, 1):
        print(f"\n{i}. {case['name']}")
        print(f"   Description: {case['description']}")
        print(f"   Example: {case['example']}")


def show_comparison():
    """Show comparison of queue implementations."""
    print("\n" + "="*80)
    print("QUEUE IMPLEMENTATIONS COMPARISON")
    print("="*80)
    
    print("\n┌─ BASIC QUEUE (List-based)")
    print("│  Enqueue: O(1)")
    print("│  Dequeue: O(n) ⚠️ Slow due to list.pop(0)")
    print("│  Peek: O(1)")
    print("│  Use: Simple cases")
    print("└──────────────────────────────")
    
    print("\n┌─ OPTIMIZED QUEUE (Deque-based)")
    print("│  Enqueue: O(1)")
    print("│  Dequeue: O(1) ⭐ Much faster!")
    print("│  Peek: O(1)")
    print("│  Use: Production systems")
    print("└──────────────────────────────")
    
    print("\n┌─ BOUNDED QUEUE")
    print("│  Enqueue: O(1) with overflow check")
    print("│  Dequeue: O(n) or O(1)")
    print("│  Peek: O(1)")
    print("│  Use: Fixed size buffers")
    print("└──────────────────────────────")
    
    print("\n┌─ LINKED LIST QUEUE")
    print("│  Enqueue: O(1)")
    print("│  Dequeue: O(1)")
    print("│  Peek: O(1)")
    print("│  Use: Dynamic size, no overflow")
    print("└──────────────────────────────")
    
    print("\n┌─ PRIORITY QUEUE")
    print("│  Enqueue: O(n) due to sorting")
    print("│  Dequeue: O(1)")
    print("│  Peek: O(1)")
    print("│  Use: Priority-based processing")
    print("└──────────────────────────────")


def benchmark_queues():
    """Performance benchmark of different queue types."""
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK (10,000 operations)")
    print("="*80)
    
    import time
    
    iterations = 10000
    
    print("\n1. Basic Queue (List-based):")
    q1 = Queue()
    start = time.time()
    for i in range(iterations):
        q1.enqueue(i)
    for i in range(iterations):
        q1.dequeue()
    elapsed = time.time() - start
    print(f"   Time: {elapsed:.4f}s")
    
    print("\n2. Optimized Queue (Deque-based):")
    q2 = OptimizedQueue()
    start = time.time()
    for i in range(iterations):
        q2.enqueue(i)
    for i in range(iterations):
        q2.dequeue()
    elapsed = time.time() - start
    print(f"   Time: {elapsed:.4f}s ⭐ FASTER")
    
    print("\n3. Linked List Queue:")
    q3 = LinkedListQueue()
    start = time.time()
    for i in range(iterations):
        q3.enqueue(i)
    for i in range(iterations):
        q3.dequeue()
    elapsed = time.time() - start
    print(f"   Time: {elapsed:.4f}s")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("="*80)
    print("QUEUE DATA STRUCTURE - COMPREHENSIVE IMPLEMENTATION")
    print("="*80)
    
    print("\nSelect demonstration or interactive mode:")
    print("1. Demonstration 1: Basic Queue")
    print("2. Demonstration 2: Optimized Queue")
    print("3. Demonstration 3: Bounded Queue")
    print("4. Demonstration 4: Typed Queue")
    print("5. Demonstration 5: Priority Queue")
    print("6. Demonstration 6: Linked List Queue")
    print("7. Demonstration 7: Producer-Consumer Pattern")
    print("8. Show Use Cases")
    print("9. Show Comparison")
    print("10. Performance Benchmark")
    print("11. Interactive Mode - Basic Queue")
    print("12. Interactive Mode - Optimized Queue")
    print("13. Interactive Mode - Bounded Queue")
    print("14. Interactive Mode - Typed Queue")
    print("15. Interactive Mode - Priority Queue")
    print("16. Interactive Mode - Linked List Queue")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-16): ").strip()
        
        if choice == "1":
            demonstrate_basic_queue()
        elif choice == "2":
            demonstrate_optimized_queue()
        elif choice == "3":
            demonstrate_bounded_queue()
        elif choice == "4":
            demonstrate_typed_queue()
        elif choice == "5":
            demonstrate_priority_queue()
        elif choice == "6":
            demonstrate_linked_list_queue()
        elif choice == "7":
            demonstrate_producer_consumer()
        elif choice == "8":
            show_use_cases()
        elif choice == "9":
            show_comparison()
        elif choice == "10":
            benchmark_queues()
        elif choice == "11":
            menu = QueueMenu("basic")
            menu.run()
        elif choice == "12":
            menu = QueueMenu("optimized")
            menu.run()
        elif choice == "13":
            menu = QueueMenu("bounded")
            menu.run()
        elif choice == "14":
            menu = QueueMenu("typed")
            menu.run()
        elif choice == "15":
            menu = QueueMenu("priority")
            menu.run()
        elif choice == "16":
            menu = QueueMenu("linkedlist")
            menu.run()
        elif choice == "0":
            print("\n✓ Thank you for using Queue Implementation!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()