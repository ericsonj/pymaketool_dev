/*
 * main.c
 *
 *  Created on: 2021/26/01 09:13:02
 *      Author: Ericson Joseph
 */

#include <stdio.h>
#include "lib.h"
#include "module_lib.h"
#if __TEST_DEFINE__
#include <stdint.h>
#else
#endif
#include "main.h"

#define DECL_HTTP_REQUEST
#include "mod.h"

int main(int argc, const char* argv[]) {

    LIB_test("HOLA");

    module_lib_sum(1, 2);

    printf("%s", HTTP_REQUEST[0]);

#if __TEST_DEFINE__
    printf("\nHello, Define!\n");
#else
    printf("Hello, World!\n");
#endif
    return 0;
}
