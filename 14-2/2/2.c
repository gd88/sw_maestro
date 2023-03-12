#include <stdio.h>
#include <stdlib.h>

#define MAX_PTR 2

// ���� �Ҵ� ���� �޸� ������ ���� �ּҸ� ������ �迭
void* allocPtrList[MAX_PTR];

// ��� �迭�� ����� ���� �Ҵ� ���� ���� ��
// clearPtrList() �Լ� ȣ�� �� �ٽ� 0���� ����
int ptrCnt = 0;

// ���� �Ҵ� ���� ��� �޸𸮸� ����
void clearPtrList() {
    for (int i = 0; i < ptrCnt; i++)
        free(allocPtrList[i]);

    ptrCnt = 0;
}

// �־��� size��ŭ ���� �Ҵ� �޾� �� ���� �ּҸ� ��ȯ
void* allocatePtr(int size) {
    // �̹� �ִ� ������ŭ �Ҵ� ���� ���
    // ������ �Ҵ� ���� ��� �޸𸮸� ����
    if (ptrCnt == MAX_PTR) {
        printf("Freeing all allocated memories...\n");
        clearPtrList();
    }

    // �Ҵ��� �޸� ũ�Ⱑ 0���� ū�� ����
    if (size <= 0) {
        printf("Invalid allocation size: %d\n", size);
        exit(0);
    }

    // size��ŭ�� �޸� ������ ���� �Ҵ�
    void* ptr = malloc(size);

    // ���� �Ҵ翡 �����ߴ��� ����
    if (!ptr) {
        printf("Memory allocation failed!\n");
        exit(0);
    }

    // �Ҵ�� �޸� �ּҸ� �����ϴ� �迭�� �� �ּҸ� ����
    // �̶� �Ҵ� Ƚ���� 1 ����
    allocPtrList[ptrCnt++] = ptr;

    // �Ҵ� ���� �޸� �ּ� ��ȯ
    return ptr;
}

int main() {
    int arrLen = 3;
    int i;

    int* intArr = (int*)allocatePtr(sizeof(int) * arrLen);
    double* doubleArr = (double*)allocatePtr(sizeof(double) * arrLen);
    
    for (i = 0; i <= 2; i++)
        intArr[i] = i;

    char* charArr1 = (char*)allocatePtr(sizeof(char) * arrLen);
    char* charArr2 = (char*)allocatePtr(sizeof(char) * arrLen);



    char* charArr3 = (char*)allocatePtr(sizeof(char) * arrLen);
    for (i = 0; i < arrLen; i++)
        charArr3[i] = '0' + i;

    free(charArr3);

    return 0;
}