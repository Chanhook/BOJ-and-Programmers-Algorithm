#include <stdio.h>
#include <stdlib.h>
#define SMAX 100001
#define TRUE 1
#define FALSE 0

typedef int SData;

typedef struct _stack{
    SData* arr;
    int index;
} Stack;

void SInit(Stack* stack)
{
    stack->arr = (SData*)malloc(sizeof(SData)*SMAX);
    stack->index = -1;
}

void SPush(Stack* stack, SData data)
{
    /*f(stack->index == SMAX-1)
    {
        printf("No space in stack.\n");
        exit(-1);
    }*/
    stack->arr[++(stack->index)] = data;
}

int SEmpty(Stack stack)
{
    if(stack.index == -1) return 1;
    else return 0;
}

int SSize(Stack stack)
{
    return stack.index + 1;
}

void SPop(Stack* stack)
{
    stack->index--;
}

SData SPeek(Stack stack)
{
    if(SEmpty(stack)) return -1;
    return stack.arr[stack.index];
}

int sequence[100001];
int order[200002];

int main()
{
    /*
    문제
    스택 (stack)은 기본적인 자료구조 중 하나로, 
    컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
    스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아
    제일 나중에 들어간 자료가 제일 먼저 나오는 
    (LIFO, Last in First out) 특성을가지고 있다.

    1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 
    하나의 수열을 만들 수 있다. 
    이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
    임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
    있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
    이를 계산하는 프로그램을 작성하라.

    입력
    첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
    둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 
    하나씩 순서대로 주어진다. 
    물론 같은 정수가 두 번 나오는 일은 없다.

    출력
    입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
    push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
    
    */
    
    int n;
    int num;
    int impossible = FALSE;
    int index = 0;
    int sqindex = 1;
    Stack stack;
    SInit(&stack);
    scanf("%d", &n);
    
    for(int i=1; i<=n; i++)
    {
        scanf("%d", &num);
        sequence[i] = num;
    }
    
    int i=1;
    
    while(sqindex <= n)
    {
        if(i < sequence[sqindex])//현재 넣을 수 있는 수가 sequence의 값보다 작다면
        {
            SPush(&stack, i);
            order[index++] = '+';
            i++;
        }
        else if(i == sequence[sqindex])//현재 넣으려는 수가 sequence의 수와 같다면
        {
            SPush(&stack, i);
            order[index++] = '+';
            i++;
            SPop(&stack);
            order[index++] = '-';
            sqindex++;
        }
        else //현재 넣으려는 수가 sequence의 수보다 크다면
        {
            if(SPeek(stack) == sequence[sqindex]) //스택의 가장 위에 있는 수가 sequence의 수와 같다면
            {
                SPop(&stack);
                order[index++] = '-';
                sqindex++;
            }
            else
            {
                impossible = TRUE;
                break;
            }
        }
    }
    
    if(impossible == FALSE)
    {
        for(int i=0; i<index; i++)
            printf("%c\n", order[i]);
    }
    else
        printf("NO\n");
        
}