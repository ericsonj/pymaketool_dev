/*
 * main.c
 *
 *  Created on: 2021/26/01 09:13:02
 *      Author: Ericson Joseph
 */

#include <stdio.h>
#include "lib.h"

int main(int argc, const char* argv[]) {

    LIB_test("HOLA");

#if __TEST_DEFINE__
    printf("Hello, Define!\n");
#else
    printf("Hello, World!\n");
#endif
    return 0;
}