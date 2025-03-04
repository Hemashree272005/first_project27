#include <stdio.h>
#include <string.h>
#define N 100

char s[N];
int t = -1;
char g[N][N];
int n;
char v;
char a[10];
int top = -1, i;

void push(char c)
{
    s[++t] = c;
}

void pop(int x)
{
    t -= x;
}

void display()
{
    for (int i = 0; i <= t; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}

int reduce_once()
{
    for (int i = 0; i < n; i++)
    {
        int l = strlen(g[i]) - 3;
        if (l <= t + 1)
        {
            if (strncmp(&s[t - l + 1], &g[i][3], l) == 0)
            {
                pop(l);
                push(g[i][0]);
                return 1;
            }
        }
    }
    return 0;
}

void reduce_all()
{
    int c = 0;
    while (reduce_once())
    {
        c++;
        if (c > 100)
        {
            break;
        }
    }
}

int parse(char *m)
{
    int l = strlen(m);
    for (int i = 0; i < l; i++)
    {
        push(m[i]);
        printf("Shift: ");
        display();
        reduce_all();
        printf("Reduce: ");
        display();
    }
    return (t == 0 && s[t] == v);
}

void error()
{
    printf("Syntax Error");
}

void push_stack(char k[])
{
    for (i = 0; k[i] != '\0'; i++)
    {
        if (top < 9)
            a[++top] = k[i];
    }
}

char TOS()
{
    return a[top];
}

void pop_stack()
{
    if (top >= 0)
        a[top--] = '\0';
}

void display_stack()
{
    for (i = 0; i <= top; i++)
        printf("%c", a[i]);
}

void display_input(char p[], int m)
{
    int l;
    printf("\t");
    for (l = m; p[l] != '\0'; l++)
        printf("%c", p[l]);
}

char* stack()
{
    return a;
}

int main()
{
    printf("Enter the number of grammar rules: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s", g[i]);
    }
    v = g[0][0];
    char m[N];
    printf("Enter the input string: ");
    scanf("%s", m);
    if (parse(m))
    {
        printf("String is accepted by the grammar.\n");
    }
    else
    {
        printf("String is not accepted by the grammar.\n");
    }
    return 0;
}
