#include <stdio.h>

struct Node{ //stores data and a pointer to the next structure as well
    int number;
    struct Node *next;
};

void print_list(struct Node *node)
{
    while(node != NULL)
    {
        printf("%d->", node->number); //imitates the structure of linked list
        // as we reach one after another by accessing structure members using ->
        node = node->next;
    }
    printf("NULL\n");
}

void insert_node (struct Node *node,
        struct Node *new)
{
    struct Node* last = node->next;
    node->next = new;
    new->next = last;

}

void delete_node(struct Node* all, struct Node* node)
{
    struct Node* copy = all;
    while(copy->next != node)
    {
        copy = copy->next;
    }
    copy->next = node->next;
}

int main()
{
    struct Node node1;
    node1.number = 9;
    struct Node node2;
    node2.number = 8;
    node2.next = NULL;
    node1.next = &node2;
    print_list(&node1);
    struct Node node3;
    node3.number = 5;
    insert_node(&node2, &node3);
    print_list(&node1);
    delete_node(&node1, &node2);
    print_list(&node1);
    return 0;
}
