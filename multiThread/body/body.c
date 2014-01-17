#include <stdio.h>
#include <pthread.h>

/* This is the body of human. */
void body(void)
{
    int i;

    for (i = 0; i < 100; i++) {
        printf("This is in body.\n");
        sleep(1);
    }
}

int body_init(pthread_t *trd_body)
{
    int ret;

    ret = pthread_create(trd_body, NULL, (void *)body, NULL);

    if (ret != 0) {
        printf("Create body error!\n");
        return 1;
    }

    return 0;
}
