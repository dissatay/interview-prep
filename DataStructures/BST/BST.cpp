#include <stdio.h>
#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node* left;
        Node* right;
        Node* parent;

        Node(int data = 0, Node* left = nullptr, Node* right = nullptr, Node* parent = nullptr) : 
                data(data), left(left), right(right), parent(parent) {}
        ~Node() {
            free(left);
            left = nullptr;
            free(right);
            right = nullptr;
            free(parent);
            parent = nullptr;
        }

        void insertN(int data) {
            Node** targetPtr = (data <= this->data) ? &this->left : &this->right;
            if(!*targetPtr) {
                *targetPtr = new Node(data, this);
                return;
            }
            (**targetPtr).insertN(data);
        }

        void preOrderN() {
            cout << data << "\n";
            if (left) (*left).inOrderN();
            if (right) (*right).inOrderN();
            return;
        }
        void inOrderN() {
            if (left) (*left).inOrderN();
            cout << data << "\n";
            if (right) (*right).inOrderN();
            return;
        }
        void postOrderN() {
            if (left) (*left).inOrderN();
            if (right) (*right).inOrderN();
            cout << data << "\n";
            return;
        }
};

enum print_opt(preOrder, inOrder, postOrder);

class Tree {
    private: 
        Node* lookupH(Node* node, int data) {
            if(!node) {
                return nullptr;
            }
            if (data == node-> data) return node;
            (data < node->data)? return lookupH(node->left, data) : return lookupH(node->right, data);  
        }

        void removeH(Node* node) {
            if(node-> left && node->right) {
                Node* scsr = successor(node); 
                node->data = scsr->data;
                removeH(scsr);
                return;
            }
            if(node->parent) Node** parentSide = (node->parent == node->parent->left) ? &node->parent->left : &node->parent->right;
            if(node->left) {
                if(node->parent) (*parentSide) = node->left;
                else root = node->left;
            }
            else if(node->right) {
                if(node->parent) (*parentSide) = node->right;
                else root = node->right;
            }
            else {
                if(node->parent) (*parentSide) = nullptr;
                else root = nullptr;
            }
            delete(node);
        }

        int getHeightH(Node* node) {
            if(!node->left && !node->right) return 0;
            if(node->left && node->right) return 1 + max(getHeightH(node->left), getHeight(node->right));
            if(node->left) return 1 + getHeightH(node->left);
            if(node->right) return 1 + getHeightH(node->right);
        }

       
    public:
        Node* root;
        Tree() {root = nullptr;}
            
        void insert(int data) {
            if (!this->root) {
                this->root = new Node(data);
                return;
            }
            (*root).insertN(data);
        }

        void print(int option) {
            if(!this->root) {
                cout << "empty tree\n";
            }
            if(option == preOrder)(*this->root).preOrderN();
            if(option == inOrder)(*this->root).inOrderN();
            if(option == postOrder)(*this->root).postOrderN();
        }

/*
    0 - not found 1 - found
 */
        int lookup(data) {
           if(!this->root) return 0; 
           lookupH(root, data);
        }

/*
 can return null if no successor
 */        
        Node* successor(Node* n) {
            if(n->right) {
                Node* currNode = n->right;
                whle(currNode->left) {
                    currNode = currNode->lef;
                }
                return currNode
            }
            if(n->parent) {
                Node* currNode = n;
                Node* currPrnt - n->parent;
                while(currPrnt) {
                    if(currPrnt->left == currNode) {
                        return currPrnt;
                    }
                    currNode = currNode -> parent;
                    currPrnt = currNOde -> parent;
                }
            }
            return nullptr;
        }

        void remove(data) {
            Node* toRemove = lookup(data);
            if(!toRemove) return;
            removeH(toRemove);
        }

        int getHeight() {
           if(!this->root) return -1; 
           getHeightH(root);
        }


};

int main() {
    Tree* treePtr = new Tree();
    Tree tree = *treePtr;
    tree.insert(1);
    tree.insert(2);
    tree.insert(3);
    tree.inOrder();
}





