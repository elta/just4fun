
CROSS_COMPILE	?= mips64el-unknown-linux-gnu-

SIM = qemu-system-mips64el
SIMFLAGS = -nographic -M malta -kernel

AS      = $(CROSS_COMPILE)as
LD      = $(CROSS_COMPILE)ld
CC      = $(CROSS_COMPILE)gcc
AR      = $(CROSS_COMPILE)ar
NM      = $(CROSS_COMPILE)nm
STRIP       = $(CROSS_COMPILE)strip
RANLIB      = $(CROSS_COMPILE)ranlib
OBJCOPY     = $(CROSS_COMPILE)objcopy
OBJDUMP     = $(CROSS_COMPILE)objdump

VECTORS_OBJ ?= ./head.o ./printf.o

HEAD_FLAGS ?= -nostdinc -mabi=64 -G 0 -mno-abicalls -fno-pic -pipe \
              -msoft-float -march=mips64 -Wa,-mips64 -Wa,--trap \
              -msym32 -DKBUILD_64BIT_SYM32 -I./

CFLAGS ?= -nostdinc -mabi=64 -G 0 -mno-abicalls -fno-pic -fno-builtin  \
          -pipe -march=mips64r2 -mgp64 -mdsp -static -Wa,--trap -msym32 \
          -DKBUILD_64BIT_SYM32 -I./

LDFLAGS = -T./mips_boot.lds -L./
FLAGS = -nostdlib -mabi=64 -march=mips64r2 -mgp64 -mdsp

TESTCASES = main.tst

all: build

head.o : head.S
	$(Q)$(CC) $(HEAD_FLAGS) -D"STACK_TOP=0xffffffff80200000" -c $< -o $@

%.o  : %.S
	$(CC) $(CFLAGS) -c $< -o $@

%.o  : %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.tst: %.o $(VECTORS_OBJ)
	$(CC) $(VECTORS_OBJ) $(FLAGS) $(LDFLAGS) $< -o $@

build: $(VECTORS_OBJ) $(MIPSSOC_LIB) $(TESTCASES)

check:  $(VECTORS_OBJ) $(MIPSSOC_LIB) $(TESTCASES)
	@for case in $(TESTCASES); do \
		echo $(SIM) $(SIMFLAGS) ./$$case; \
		$(SIM) $(SIMFLAGS) ./$$case & (sleep 1; killall $(SIM)); \
	done

clean:
	$(Q)rm -f *.o *.tst *.a
