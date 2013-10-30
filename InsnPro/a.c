/* Fix point add/sub instructions. */
/* vpaddb 010010 00000 vt vs vd 00 0000 */
{"vpaddb", "@D,@S,@T", 0x48000000, 0xffe0003f, 0, 0, I1 },

/* Translate instructions. */
/* bc2f 111010 00000 00000 offset16 */
{"bc2f", "p", 0xe8000000, 0xffff0000, 0, 0, I1 },
