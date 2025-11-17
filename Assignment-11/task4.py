"""
Binary Search Tree (BST) Implementation

A comprehensive implementation of a Binary Search Tree data structure with:
- insert(): Add node to BST maintaining BST property
- inorder_traversal(): Display nodes in sorted order (Left-Root-Right)
- preorder_traversal(): Display nodes in preorder (Root-Left-Right)
- postorder_traversal(): Display nodes in postorder (Left-Right-Root)
- search(): Find node with specific value
- delete(): Remove node from BST
- find_min(): Find minimum value
- find_max(): Find maximum value
- height(): Get tree height
- is_balanced(): Check if tree is balanced
- Interactive menu system

A BST is a binary tree where each node has at most two children,
and for each node, all values in left subtree < node value < all values in right subtree.
"""

import logging
from typing import Any, Optional, List, Tuple
from enum import Enum
from collections import deque


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

class BSTError(Exception):
    """Base exception for BST operations."""
    pass


class NodeNotFoundError(BSTError):
    """Raised when node is not found."""
    pass


class DuplicateValueError(BSTError):
    """Raised when inserting duplicate value."""
    pass


class EmptyTreeError(BSTError):
    """Raised when operating on empty tree."""
    pass


# ============================================================================
# NODE CLASS
# ============================================================================

class BSTNode:
    """
    Node class for Binary Search Tree.
    
    Attributes
    ----------
    value : int or float or comparable
        Value stored in the node.
    left : BSTNode or None
        Reference to left child node.
    right : BSTNode or None
        Reference to right child node.
    """
    
    def __init__(self, value: Any):
        """
        Initialize a BST node.
        
        Parameters
        ----------
        value : Any
            Value to store in the node.
        """
        self.value = value
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None
        logger.debug(f"✓ BSTNode created with value: {value}")
    
    def __str__(self) -> str:
        """String representation of node."""
        return str(self.value)
    
    def __repr__(self) -> str:
        """Detailed representation of node."""
        return f"BSTNode({self.value})"


# ============================================================================
# BINARY SEARCH TREE IMPLEMENTATION V1: BASIC BST
# ============================================================================

class BinarySearchTree:
    """
    Binary Search Tree implementation.
    
    A binary tree where for each node:
    - All values in left subtree < node value
    - All values in right subtree > node value
    
    Attributes
    ----------
    root : BSTNode or None
        Reference to the root node of the tree.
    
    Methods
    -------
    insert(value)
        Add value to tree maintaining BST property.
    inorder_traversal()
        Return values in sorted order (Left-Root-Right).
    preorder_traversal()
        Return values in preorder (Root-Left-Right).
    postorder_traversal()
        Return values in postorder (Left-Right-Root).
    levelorder_traversal()
        Return values level by level.
    search(value)
        Find and return node with specific value.
    delete(value)
        Remove node with specific value.
    find_min()
        Find minimum value in tree.
    find_max()
        Find maximum value in tree.
    height()
        Get height of tree.
    is_balanced()
        Check if tree is balanced.
    display()
        Show tree structure visually.
    
    Examples
    --------
    >>> bst = BinarySearchTree()
    >>> bst.insert(50)
    >>> bst.insert(30)
    >>> bst.insert(70)
    >>> bst.insert(20)
    >>> bst.insert(40)
    >>> bst.inorder_traversal()
    [20, 30, 40, 50, 70]
    """
    
    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[BSTNode] = None
        logger.info("✓ Binary Search Tree created")
    
    def insert(self, value: Any) -> None:
        """
        Insert value into BST maintaining BST property.
        
        Parameters
        ----------
        value : Any
            Value to insert.
        
        Returns
        -------
        None
        
        Raises
        ------
        DuplicateValueError
            If value already exists in tree.
        
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(log n) average, O(n) worst case (recursion stack)
        
        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(50)
        >>> bst.insert(30)
        >>> bst.insert(70)
        """
        if self.root is None:
            self.root = BSTNode(value)
            logger.info(f"✓ Inserted {value} as root")
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: BSTNode, value: Any) -> None:
        """
        Recursively insert value into BST.
        
        Parameters
        ----------
        node : BSTNode
            Current node in traversal.
        value : Any
            Value to insert.
        
        Raises
        ------
        DuplicateValueError
            If value already exists.
        """
        if value == node.value:
            error_msg = f"Duplicate value: {value} already exists in tree"
            logger.error(f"✗ {error_msg}")
            raise DuplicateValueError(error_msg)
        
        # Insert in left subtree
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
                logger.info(f"✓ Inserted {value} to left of {node.value}")
            else:
                self._insert_recursive(node.left, value)
        
        # Insert in right subtree
        else:
            if node.right is None:
                node.right = BSTNode(value)
                logger.info(f"✓ Inserted {value} to right of {node.value}")
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self) -> List[Any]:
        """
        Traversal in order: Left - Root - Right (Sorted order).
        
        Returns
        -------
        List[Any]
            Values in sorted order.
        
        Time Complexity: O(n)
        Space Complexity: O(h) where h is height
        
        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> for val in [50, 30, 70, 20, 40]:
        ...     bst.insert(val)
        >>> bst.inorder_traversal()
        [20, 30, 40, 50, 70]
        """
        result = []
        self._inorder_recursive(self.root, result)
        logger.info(f"✓ Inorder traversal: {result}")
        return result
    
    def _inorder_recursive(self, node: Optional[BSTNode], result: List) -> None:
        """
        Recursively traverse in inorder.
        
        Parameters
        ----------
        node : BSTNode or None
            Current node.
        result : List
            List to store traversal result.
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[Any]:
        """
        Traversal in preorder: Root - Left - Right.
        
        Returns
        -------
        List[Any]
            Values in preorder.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Use case: Copy of tree, expression trees
        """
        result = []
        self._preorder_recursive(self.root, result)
        logger.info(f"✓ Preorder traversal: {result}")
        return result
    
    def _preorder_recursive(self, node: Optional[BSTNode], result: List) -> None:
        """Recursively traverse in preorder."""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[Any]:
        """
        Traversal in postorder: Left - Right - Root.
        
        Returns
        -------
        List[Any]
            Values in postorder.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        
        Use case: Delete tree, expression evaluation
        """
        result = []
        self._postorder_recursive(self.root, result)
        logger.info(f"✓ Postorder traversal: {result}")
        return result
    
    def _postorder_recursive(self, node: Optional[BSTNode], result: List) -> None:
        """Recursively traverse in postorder."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def levelorder_traversal(self) -> List[Any]:
        """
        Level order traversal (Breadth-First).
        
        Returns
        -------
        List[Any]
            Values level by level.
        
        Time Complexity: O(n)
        Space Complexity: O(w) where w is max width
        """
        if self.root is None:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        logger.info(f"✓ Level order traversal: {result}")
        return result
    
    def search(self, value: Any) -> Optional[BSTNode]:
        """
        Search for node with specific value.
        
        Parameters
        ----------
        value : Any
            Value to search for.
        
        Returns
        -------
        Optional[BSTNode]
            Node if found, None otherwise.
        
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(log n) recursion stack
        
        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(50)
        >>> node = bst.search(50)
        >>> node is not None
        True
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: Optional[BSTNode], value: Any) -> Optional[BSTNode]:
        """Recursively search for value."""
        if node is None:
            logger.warning(f"⚠ Value {value} not found in tree")
            return None
        
        if value == node.value:
            logger.info(f"✓ Found node with value: {value}")
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def find_min(self) -> Optional[Any]:
        """
        Find minimum value in tree.
        
        Returns
        -------
        Optional[Any]
            Minimum value, None if tree is empty.
        
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(1)
        
        Note: Minimum is always the leftmost node.
        """
        if self.root is None:
            logger.warning("⚠ Tree is empty")
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        
        logger.info(f"✓ Minimum value: {current.value}")
        return current.value
    
    def find_max(self) -> Optional[Any]:
        """
        Find maximum value in tree.
        
        Returns
        -------
        Optional[Any]
            Maximum value, None if tree is empty.
        
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(1)
        
        Note: Maximum is always the rightmost node.
        """
        if self.root is None:
            logger.warning("⚠ Tree is empty")
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        
        logger.info(f"✓ Maximum value: {current.value}")
        return current.value
    
    def delete(self, value: Any) -> bool:
        """
        Delete node with specific value from BST.
        
        Parameters
        ----------
        value : Any
            Value to delete.
        
        Returns
        -------
        bool
            True if deleted, False if not found.
        
        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(log n) recursion stack
        
        Cases handled:
        1. Node has no children (leaf)
        2. Node has one child
        3. Node has two children (inorder successor)
        """
        if self.root is None:
            logger.warning("⚠ Tree is empty")
            return False
        
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted
    
    def _delete_recursive(self, node: Optional[BSTNode], value: Any) -> Tuple[Optional[BSTNode], bool]:
        """Recursively delete node with value."""
        if node is None:
            logger.warning(f"⚠ Value {value} not found in tree")
            return None, False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted
        else:
            # Node found, delete it
            logger.info(f"✓ Deleting node with value: {value}")
            
            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None, True
            
            # Case 2: Only right child
            if node.left is None:
                return node.right, True
            
            # Case 3: Only left child
            if node.right is None:
                return node.left, True
            
            # Case 4: Both children - find inorder successor
            # (minimum value in right subtree)
            successor_parent = node
            successor = node.right
            
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            # Replace node value with successor value
            node.value = successor.value
            
            # Delete successor
            if successor_parent == node:
                node.right = successor.right
            else:
                successor_parent.left = successor.right
            
            return node, True
    
    def height(self) -> int:
        """
        Get height of tree.
        
        Returns
        -------
        int
            Height of tree (empty tree = -1, single node = 0).
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node: Optional[BSTNode]) -> int:
        """Recursively calculate height."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def is_balanced(self) -> bool:
        """
        Check if tree is balanced.
        
        A tree is balanced if for every node, the height difference
        between left and right subtrees is at most 1.
        
        Returns
        -------
        bool
            True if tree is balanced, False otherwise.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def check_balance(node: Optional[BSTNode]) -> Tuple[bool, int]:
            """Check if node's subtree is balanced and return (is_balanced, height)."""
            if node is None:
                return True, -1
            
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            
            # Check balance at this node
            is_balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return is_balanced, height
        
        is_balanced_result, _ = check_balance(self.root)
        logger.info(f"✓ Tree is {'balanced' if is_balanced_result else 'not balanced'}")
        return is_balanced_result
    
    def is_empty(self) -> bool:
        """
        Check if tree is empty.
        
        Returns
        -------
        bool
            True if tree is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.root is None
    
    def clear(self) -> None:
        """
        Clear all nodes from tree.
        
        Time Complexity: O(1) - nodes are garbage collected
        Space Complexity: O(1)
        """
        self.root = None
        logger.info("✓ Tree cleared")
    
    def __len__(self) -> int:
        """
        Get number of nodes in tree.
        
        Returns
        -------
        int
            Number of nodes.
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        return self._count_nodes(self.root)
    
    def _count_nodes(self, node: Optional[BSTNode]) -> int:
        """Recursively count nodes."""
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    
    def display(self) -> None:
        """
        Display tree structure visually.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.root is None:
            print("  Tree is empty")
            return
        
        print("\n  Tree Structure:")
        self._display_recursive(self.root, "", True)
        print()
    
    def _display_recursive(self, node: Optional[BSTNode], prefix: str, is_last: bool) -> None:
        """Recursively display tree structure."""
        if node is None:
            return
        
        print(prefix + ("└── " if is_last else "├── ") + str(node.value))
        
        children = [node.left, node.right]
        children_count = sum(1 for child in children if child is not None)
        
        for i, child in enumerate(children):
            if child is not None:
                extension = "    " if is_last else "│   "
                self._display_recursive(child, prefix + extension, i == children_count - 1)
    
    def to_list(self) -> List[Any]:
        """
        Convert tree to list (inorder).
        
        Returns
        -------
        List[Any]
            Sorted list of values.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return self.inorder_traversal()
    
    def __str__(self) -> str:
        """String representation."""
        if self.is_empty():
            return "BST: []"
        return f"BST: {self.inorder_traversal()}"
    
    def __repr__(self) -> str:
        """Detailed representation."""
        return f"BinarySearchTree({self.inorder_traversal()})"


# ============================================================================
# BINARY SEARCH TREE IMPLEMENTATION V2: SELF-BALANCING (AVL TREE)
# ============================================================================

class AVLTree(BinarySearchTree):
    """
    Self-balancing Binary Search Tree (AVL Tree).
    
    Maintains height difference between subtrees <= 1.
    Provides O(log n) guarantee for all operations.
    """
    
    def __init__(self):
        """Initialize AVL tree."""
        super().__init__()
        logger.info("✓ AVL Tree created")
    
    def insert(self, value: Any) -> None:
        """Insert value with auto-balancing."""
        try:
            self.root = self._insert_avl(self.root, value)
        except DuplicateValueError:
            raise
    
    def _insert_avl(self, node: Optional[BSTNode], value: Any) -> BSTNode:
        """Insert and balance."""
        # Standard BST insertion
        if node is None:
            return BSTNode(value)
        
        if value == node.value:
            raise DuplicateValueError(f"Duplicate value: {value}")
        
        if value < node.value:
            node.left = self._insert_avl(node.left, value)
        else:
            node.right = self._insert_avl(node.right, value)
        
        # Balance the tree
        return self._balance(node)
    
    def _balance(self, node: BSTNode) -> BSTNode:
        """Balance node and return new root."""
        balance_factor = self._get_balance_factor(node)
        
        # Left heavy
        if balance_factor > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right heavy
        if balance_factor < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _get_balance_factor(self, node: Optional[BSTNode]) -> int:
        """Calculate balance factor."""
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return left_height - right_height
    
    def _rotate_left(self, node: BSTNode) -> BSTNode:
        """Rotate left."""
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child
    
    def _rotate_right(self, node: BSTNode) -> BSTNode:
        """Rotate right."""
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child


# ============================================================================
# INTERACTIVE MENU SYSTEM
# ============================================================================

class BSTMenu:
    """Interactive menu system for BST operations."""
    
    def __init__(self, tree_type: str = "basic"):
        """
        Initialize menu with specified tree type.
        
        Parameters
        ----------
        tree_type : str
            Type of tree: "basic" or "avl"
        """
        self.tree_type = tree_type
        
        if tree_type == "avl":
            self.tree = AVLTree()
        else:
            self.tree = BinarySearchTree()
        
        logger.info(f"✓ Menu created with {tree_type} BST")
    
    def display_menu(self):
        """Display main menu options."""
        print("\n" + "="*70)
        print("BINARY SEARCH TREE OPERATIONS MENU")
        print("="*70)
        print("1. Insert - Add value to tree")
        print("2. Search - Find value in tree")
        print("3. Inorder Traversal - Display in sorted order")
        print("4. Preorder Traversal - Display in preorder")
        print("5. Postorder Traversal - Display in postorder")
        print("6. Level Order Traversal - Display level by level")
        print("7. Display Tree - Show visual representation")
        print("8. Find Minimum - Get minimum value")
        print("9. Find Maximum - Get maximum value")
        print("10. Delete - Remove value from tree")
        print("11. Height - Get tree height")
        print("12. Is Balanced - Check if tree is balanced")
        print("13. Tree Size - Get number of nodes")
        print("14. Is Empty - Check if tree is empty")
        print("15. Clear - Remove all nodes")
        print("0. Exit")
        print("="*70)
    
    def run(self):
        """Run interactive menu system."""
        print("\n" + "="*70)
        print(f"BINARY SEARCH TREE - {self.tree_type.upper()}")
        print("="*70)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-15): ").strip()
            
            try:
                if choice == "1":
                    self._handle_insert()
                elif choice == "2":
                    self._handle_search()
                elif choice == "3":
                    self._handle_inorder()
                elif choice == "4":
                    self._handle_preorder()
                elif choice == "5":
                    self._handle_postorder()
                elif choice == "6":
                    self._handle_levelorder()
                elif choice == "7":
                    self._handle_display()
                elif choice == "8":
                    self._handle_find_min()
                elif choice == "9":
                    self._handle_find_max()
                elif choice == "10":
                    self._handle_delete()
                elif choice == "11":
                    self._handle_height()
                elif choice == "12":
                    self._handle_is_balanced()
                elif choice == "13":
                    self._handle_size()
                elif choice == "14":
                    self._handle_is_empty()
                elif choice == "15":
                    self._handle_clear()
                elif choice == "0":
                    print("\n✓ Thank you for using BST Implementation!")
                    break
                else:
                    print("\n❌ Invalid choice. Please try again.")
            
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
    
    def _handle_insert(self):
        """Handle insert operation."""
        try:
            value = input("Enter value to insert: ")
            # Try to convert to number
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            self.tree.insert(value)
            print(f"✓ Successfully inserted {value}")
        except DuplicateValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_search(self):
        """Handle search operation."""
        try:
            value = input("Enter value to search: ")
            # Try to convert to number
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            node = self.tree.search(value)
            if node:
                print(f"✓ Found: {value}")
            else:
                print(f"❌ Value {value} not found in tree")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_inorder(self):
        """Handle inorder traversal."""
        result = self.tree.inorder_traversal()
        print(f"✓ Inorder (sorted): {result}")
    
    def _handle_preorder(self):
        """Handle preorder traversal."""
        result = self.tree.preorder_traversal()
        print(f"✓ Preorder: {result}")
    
    def _handle_postorder(self):
        """Handle postorder traversal."""
        result = self.tree.postorder_traversal()
        print(f"✓ Postorder: {result}")
    
    def _handle_levelorder(self):
        """Handle level order traversal."""
        result = self.tree.levelorder_traversal()
        print(f"✓ Level order: {result}")
    
    def _handle_display(self):
        """Handle display."""
        print("\n" + "-"*70)
        self.tree.display()
        print("-"*70)
    
    def _handle_find_min(self):
        """Handle find minimum."""
        min_val = self.tree.find_min()
        if min_val is not None:
            print(f"✓ Minimum value: {min_val}")
        else:
            print("❌ Tree is empty")
    
    def _handle_find_max(self):
        """Handle find maximum."""
        max_val = self.tree.find_max()
        if max_val is not None:
            print(f"✓ Maximum value: {max_val}")
        else:
            print("❌ Tree is empty")
    
    def _handle_delete(self):
        """Handle delete operation."""
        try:
            value = input("Enter value to delete: ")
            # Try to convert to number
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            if self.tree.delete(value):
                print(f"✓ Successfully deleted {value}")
            else:
                print(f"❌ Value {value} not found in tree")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _handle_height(self):
        """Handle height operation."""
        height = self.tree.height()
        print(f"✓ Tree height: {height}")
    
    def _handle_is_balanced(self):
        """Handle balance check."""
        is_balanced = self.tree.is_balanced()
        status = "balanced" if is_balanced else "not balanced"
        print(f"✓ Tree is {status}")
    
    def _handle_size(self):
        """Handle size operation."""
        size = len(self.tree)
        print(f"✓ Tree size: {size} nodes")
    
    def _handle_is_empty(self):
        """Handle empty check."""
        is_empty = self.tree.is_empty()
        status = "empty" if is_empty else "not empty"
        print(f"✓ Tree is {status}")
    
    def _handle_clear(self):
        """Handle clear operation."""
        self.tree.clear()
        print("✓ Tree cleared successfully")


# ============================================================================
# DEMONSTRATIONS AND TESTS
# ============================================================================

def demonstrate_basic_bst():
    """Demonstrate basic BST operations."""
    print("="*80)
    print("DEMONSTRATION 1: Basic Binary Search Tree Operations")
    print("="*80)
    
    bst = BinarySearchTree()
    
    print("\n1. Checking if tree is empty:")
    print(f"   is_empty(): {bst.is_empty()}")
    
    print("\n2. Inserting values: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print("\n3. Tree structure:")
    bst.display()
    
    print("4. Inorder traversal (sorted):")
    inorder = bst.inorder_traversal()
    print(f"   {inorder}")
    
    print("\n5. Preorder traversal:")
    preorder = bst.preorder_traversal()
    print(f"   {preorder}")
    
    print("\n6. Postorder traversal:")
    postorder = bst.postorder_traversal()
    print(f"   {postorder}")
    
    print("\n7. Level order traversal:")
    levelorder = bst.levelorder_traversal()
    print(f"   {levelorder}")
    
    print("\n8. Tree statistics:")
    print(f"   Size: {len(bst)} nodes")
    print(f"   Height: {bst.height()}")
    print(f"   Is balanced: {bst.is_balanced()}")
    print(f"   Minimum: {bst.find_min()}")
    print(f"   Maximum: {bst.find_max()}")
    
    print("\n9. Searching for values:")
    search_values = [40, 100, 60]
    for val in search_values:
        node = bst.search(val)
        result = "Found" if node else "Not found"
        print(f"   Search {val}: {result}")
    
    print("\n10. Deleting value 20 (leaf node):")
    bst.delete(20)
    print(f"    Inorder after delete: {bst.inorder_traversal()}")
    bst.display()
    
    print("11. Deleting value 30 (node with two children):")
    bst.delete(30)
    print(f"    Inorder after delete: {bst.inorder_traversal()}")
    bst.display()


def demonstrate_unbalanced_tree():
    """Demonstrate unbalanced tree."""
    print("\n" + "="*80)
    print("DEMONSTRATION 2: Unbalanced vs Balanced Trees")
    print("="*80)
    
    print("\n1. Creating unbalanced tree (inserting in order):")
    unbalanced = BinarySearchTree()
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        unbalanced.insert(val)
    
    print("   Values: 1, 2, 3, 4, 5, 6, 7")
    unbalanced.display()
    
    print(f"   Height: {unbalanced.height()}")
    print(f"   Is balanced: {unbalanced.is_balanced()}")
    print(f"   ⚠️ Time complexity degrades to O(n)!")
    
    print("\n2. Creating balanced tree (random insertion):")
    balanced = BinarySearchTree()
    values = [4, 2, 6, 1, 3, 5, 7]
    
    for val in values:
        balanced.insert(val)
    
    print("   Values: 4, 2, 6, 1, 3, 5, 7")
    balanced.display()
    
    print(f"   Height: {balanced.height()}")
    print(f"   Is balanced: {balanced.is_balanced()}")
    print(f"   ⭐ Time complexity is O(log n)!")


def demonstrate_avl_tree():
    """Demonstrate AVL tree self-balancing."""
    print("\n" + "="*80)
    print("DEMONSTRATION 3: AVL Tree (Self-Balancing)")
    print("="*80)
    
    avl = AVLTree()
    
    print("\n1. Inserting values in order: 1, 2, 3, 4, 5, 6, 7")
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for val in values:
        avl.insert(val)
    
    print("\n   AVL Tree maintains balance automatically!")
    avl.display()
    
    print(f"   Height: {avl.height()}")
    print(f"   Is balanced: {avl.is_balanced()}")
    print(f"   Inorder: {avl.inorder_traversal()}")
    print(f"   ⭐ All operations guaranteed O(log n)!")


def demonstrate_traversals():
    """Demonstrate different traversal methods."""
    print("\n" + "="*80)
    print("DEMONSTRATION 4: Tree Traversal Methods")
    print("="*80)
    
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]
    
    print(f"\n1. Building tree with values: {values}")
    for val in values:
        bst.insert(val)
    
    bst.display()
    
    print("\n2. Inorder (Left-Root-Right) - Sorted order:")
    print(f"   Use case: Get sorted values")
    print(f"   Result: {bst.inorder_traversal()}")
    
    print("\n3. Preorder (Root-Left-Right) - Prefix notation:")
    print(f"   Use case: Copy of tree, expression trees")
    print(f"   Result: {bst.preorder_traversal()}")
    
    print("\n4. Postorder (Left-Right-Root) - Postfix notation:")
    print(f"   Use case: Delete tree, evaluate expression")
    print(f"   Result: {bst.postorder_traversal()}")
    
    print("\n5. Level order (Breadth-First):")
    print(f"   Use case: Level-by-level processing")
    print(f"   Result: {bst.levelorder_traversal()}")


def show_use_cases():
    """Show real-world use cases of BST."""
    print("\n" + "="*80)
    print("REAL-WORLD USE CASES OF BINARY SEARCH TREES")
    print("="*80)
    
    use_cases = [
        {
            "name": "Database Indexing",
            "description": "Index data for fast lookup",
            "example": "B-trees in SQL databases"
        },
        {
            "name": "File Systems",
            "description": "Directory structure organization",
            "example": "File hierarchy in operating systems"
        },
        {
            "name": "Expression Parsing",
            "description": "Parse mathematical expressions",
            "example": "Compiler syntax trees"
        },
        {
            "name": "Auto-Complete",
            "description": "Suggest completions while typing",
            "example": "Search engines, text editors"
        },
        {
            "name": "Range Queries",
            "description": "Find all values in a range",
            "example": "Date range searches, price range filters"
        },
        {
            "name": "Dictionary/Spell Check",
            "description": "Store and search dictionary words",
            "example": "Spell checkers, word validation"
        },
        {
            "name": "Router IP Routing",
            "description": "IP address lookup in routing tables",
            "example": "Network packet routing"
        },
        {
            "name": "Game AI",
            "description": "Decision tree for AI moves",
            "example": "Chess AI evaluation tree"
        }
    ]
    
    for i, case in enumerate(use_cases, 1):
        print(f"\n{i}. {case['name']}")
        print(f"   Description: {case['description']}")
        print(f"   Example: {case['example']}")


def show_complexity_analysis():
    """Show time complexity analysis."""
    print("\n" + "="*80)
    print("TIME COMPLEXITY ANALYSIS - BINARY SEARCH TREE")
    print("="*80)
    
    operations = [
        ("insert()", "O(log n)", "O(n)", "Balanced", "Skewed"),
        ("search()", "O(log n)", "O(n)", "Balanced", "Skewed"),
        ("delete()", "O(log n)", "O(n)", "Balanced", "Skewed"),
        ("inorder_traversal()", "O(n)", "O(n)", "All cases", "All cases"),
        ("find_min()", "O(log n)", "O(n)", "Balanced", "Skewed"),
        ("find_max()", "O(log n)", "O(n)", "Balanced", "Skewed"),
        ("height()", "O(n)", "O(n)", "All cases", "All cases"),
    ]
    
    print("\n{:<25} {:<15} {:<15} {:<20} {:<20}".format(
        "Operation", "Avg Case", "Worst Case", "Avg Note", "Worst Note"))
    print("-" * 95)
    
    for op, avg, worst, avg_note, worst_note in operations:
        print("{:<25} {:<15} {:<15} {:<20} {:<20}".format(
            op, avg, worst, avg_note, worst_note))
    
    print("\n" + "-" * 95)
    print("AVL Tree (Self-Balancing):")
    print("-" * 95)
    print("{:<25} {:<15} {:<15} {:<20}".format(
        "All operations", "O(log n)", "O(log n)", "Guaranteed ⭐"))


def benchmark_operations():
    """Benchmark BST operations."""
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK")
    print("="*80)
    
    import time
    import random
    
    size = 10000
    
    print(f"\n1. Inserting {size} random values:")
    bst = BinarySearchTree()
    values = list(range(size))
    random.shuffle(values)
    
    start = time.time()
    for val in values:
        bst.insert(val)
    elapsed = time.time() - start
    
    print(f"   Time: {elapsed:.4f}s")
    print(f"   Height: {bst.height()}")
    print(f"   Is balanced: {bst.is_balanced()}")
    
    print(f"\n2. Searching for {100} random values:")
    search_values = random.sample(values, 100)
    
    start = time.time()
    found = 0
    for val in search_values:
        if bst.search(val):
            found += 1
    elapsed = time.time() - start
    
    print(f"   Time: {elapsed:.4f}s")
    print(f"   Found: {found}/{len(search_values)}")
    
    print(f"\n3. Inorder traversal:")
    start = time.time()
    result = bst.inorder_traversal()
    elapsed = time.time() - start
    
    print(f"   Time: {elapsed:.4f}s")
    print(f"   Values retrieved: {len(result)}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("="*80)
    print("BINARY SEARCH TREE - COMPREHENSIVE IMPLEMENTATION")
    print("="*80)
    
    print("\nSelect demonstration or interactive mode:")
    print("1. Demonstration 1: Basic Operations")
    print("2. Demonstration 2: Unbalanced vs Balanced Trees")
    print("3. Demonstration 3: AVL Tree (Self-Balancing)")
    print("4. Demonstration 4: Tree Traversal Methods")
    print("5. Show Use Cases")
    print("6. Show Complexity Analysis")
    print("7. Performance Benchmark")
    print("8. Interactive Mode - Basic BST")
    print("9. Interactive Mode - AVL Tree")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "1":
            demonstrate_basic_bst()
        elif choice == "2":
            demonstrate_unbalanced_tree()
        elif choice == "3":
            demonstrate_avl_tree()
        elif choice == "4":
            demonstrate_traversals()
        elif choice == "5":
            show_use_cases()
        elif choice == "6":
            show_complexity_analysis()
        elif choice == "7":
            benchmark_operations()
        elif choice == "8":
            menu = BSTMenu("basic")
            menu.run()
        elif choice == "9":
            menu = BSTMenu("avl")
            menu.run()
        elif choice == "0":
            print("\n✓ Thank you for using BST Implementation!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()