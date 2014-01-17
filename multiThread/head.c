#include <stdio.h>
#include <pthread.h>

#include <body/body.h>

/* This is the brain, the main control of human. */
void start_brain(void)
{
    int i;

    for (i = 0; i < 100; i++) {
        printf("This is brain.\n");
        sleep(1);
    }
}

int main(void)
{
    pthread_t trd_body;
    int i,ret;

    ret = body_init(&trd_body);
    if(ret) {
        printf ("Create body failed!\n");
        return 1;
    }

    start_brain();

    pthread_join(trd_body,NULL);

    return 0;
}
