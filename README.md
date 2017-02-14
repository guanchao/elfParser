### SO文件解析工具 
####(1)usage:
python elfParser.py libdemo.so
####(2)例子：

python elfParser.py libdemo.so

输出结构如下：
```
[+] ELF Header:
e_ident:	e_ident=[file_identification=ELF, ei_class=1, ei_data=1, ei_version=1, ei_osabi=0, ei_abiversion=0, ei_pad=000000000000, ei_nident=0]
e_type: 	3
e_machine:	40
e_version:	1
e_entry:	0
e_phoff:	0x34	//Program header offset
e_shoff:	0x3124	//Section header offset
e_flags:	83886080
e_ehsize:	52	//ELF header size
e_phentsize:	32	//Program header entry size
e_phnum:	8	//Program header number
e_shentsize:	40	//Section header entry size
e_shnum:	22	//Section header number
e_shstrndx:	21	//Section header string index

[+] Section Header Table:
  #      Name                            Type            Addr            Offset          Size    ES      Flg     Lk      Inf     Al      
  [   0]                                 SHT_NULL        0x0             0x0             0x0     0       0       0       0       0       
  [   1] .interp                         SHT_PROGBITS    0x134           0x134           0x13    0       2       0       0       1       
  [   2] .dynsym                         SHT_DYNSYM      0x148           0x148           0x3e0   16      2       3       1       4       
  [   3] .dynstr                         SHT_STRTAB      0x528           0x528           0x51c   0       2       0       0       1       
  [   4] .hash                           SHT_HASH        0xa44           0xa44           0x194   4       2       2       0       4       
  [   5] .rel.dyn                        SHT_REL         0xbd8           0xbd8           0x50    8       2       2       0       4       
  [   6] .rel.plt                        SHT_REL         0xc28           0xc28           0x40    8       66      2       7       4       
  [   7] .plt                            SHT_PROGBITS    0xc68           0xc68           0x74    0       6       0       0       4       
  [   8] .text                           SHT_PROGBITS    0xcdc           0xcdc           0x1030  0       6       0       0       4       
  [   9] .ARM.extab                      SHT_PROGBITS    0x1d0c          0x1d0c          0x90    0       2       0       0       4       
  [  10] .ARM.exidx                      1879048193      0x1d9c          0x1d9c          0x138   8       130     8       0       4       
  [  11] .rodata                         SHT_PROGBITS    0x1ed4          0x1ed4          0xc     1       50      0       0       1       
  [  12] .fini_array                     15              0x3ea4          0x2ea4          0x8     0       3       0       0       4       
  [  13] .init_array                     14              0x3eac          0x2eac          0x4     0       3       0       0       1       
  [  14] .dynamic                        SHT_DYNAMIC     0x3eb0          0x2eb0          0x100   8       3       3       0       4       
  [  15] .got                            SHT_PROGBITS    0x3fb0          0x2fb0          0x50    0       3       0       0       4       
  [  16] .data                           SHT_PROGBITS    0x4000          0x3000          0xc     0       3       0       0       4       
  [  17] .bss                            SHT_NOBITS      0x400c          0x300c          0x4     0       3       0       0       4       
  [  18] .comment                        SHT_PROGBITS    0x0             0x300c          0x10    1       48      0       0       1       
  [  19] .note.gnu.gold-version          SHT_NOTE        0x0             0x301c          0x1c    0       0       0       0       4       
  [  20] .ARM.attributes                 SHT_MIPS_GPTAB  0x0             0x3038          0x2b    0       0       0       0       1       
  [  21] .shstrtab                       SHT_STRTAB      0x0             0x3063          0xc0    0       0       0       0       1       

[+] Program Header Table:
  #      Type            offset          VirtAddr        PhysAddr        FileSiz MemSiz  Flg     Align   
  [   0] PHDR            0x34            0x34            0x34            0x100   0x100   4       0x4     
  [   1] INTERP          0x134           0x134           0x134           0x13    0x13    4       0x1     
  [   2] LOAD            0x0             0x0             0x0             0x1ee0  0x1ee0  5       0x1000  
  [   3] LOAD            0x2ea4          0x3ea4          0x3ea4          0x168   0x16c   6       0x1000  
  [   4] DYNAMIC         0x2eb0          0x3eb0          0x3eb0          0x100   0x100   6       0x4     
  [   5] GNU_STACK       0x0             0x0             0x0             0x0     0x0     6       0x0     
  [   6] HIPROC          0x1d9c          0x1d9c          0x1d9c          0x138   0x138   4       0x4     
  [   7] GNU_RELRO       0x2ea4          0x3ea4          0x3ea4          0x15c   0x15c   6       0x4     

[+] Section to segment mapping:
  [   0] 
  [   1] .interp 
  [   2]  .interp .dynsym .dynstr .hash .rel.dyn .rel.plt .plt .text .ARM.extab .ARM.exidx .rodata 
  [   3] .fini_array .init_array .dynamic .got .data 
  [   4] .dynamic 
  [   5]  
  [   6] .ARM.exidx 
  [   7] .fini_array .init_array .dynamic .got 

[+] Dynamic Symbol Table:
  #      Value     Size    Type    Bind    Other   Ndx     Name    
  [   0] 0x0       0       NOTYPE  LOCAL   0       UNDEF           
  [   1] 0x0       0       FUNC    GLOBAL  0       UNDEF   __cxa_finalize
  [   2] 0x0       0       FUNC    GLOBAL  0       UNDEF   __cxa_atexit
  [   3] 0xd21     16      FUNC    GLOBAL  0       8       _Z15extern_functionv
  [   4] 0x4008    4       OBJECT  GLOBAL  0       16      extern_var
  [   5] 0x147d    10      FUNC    GLOBAL  0       8       __aeabi_unwind_cpp_pr0
  [   6] 0xd31     32      FUNC    GLOBAL  0       8       _Z3barv 
  [   7] 0x400c    4       OBJECT  GLOBAL  0       17      global_unint_var
  [   8] 0xd51     24      FUNC    GLOBAL  0       8       Java_com_demo_MainActivity_test
  [   9] 0x0       0       FUNC    GLOBAL  0       UNDEF   printf  
  [  10] 0x1487    10      FUNC    WEAK    0       8       __aeabi_unwind_cpp_pr1
  [  11] 0x4004    4       OBJECT  GLOBAL  0       16      global_init_var
  [  12] 0x1491    10      FUNC    WEAK    0       8       __aeabi_unwind_cpp_pr2
  [  13] 0x0       0       FUNC    WEAK    0       UNDEF   __gnu_Unwind_Find_exidx
  [  14] 0x170c    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Restore_VFP_D
  [  15] 0x16fc    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Restore_VFP
  [  16] 0x171c    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Restore_VFP_D_16_to_31
  [  17] 0x172c    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Restore_WMMXD
  [  18] 0x17b4    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Restore_WMMXC
  [  19] 0x0       0       FUNC    GLOBAL  0       UNDEF   abort   
  [  20] 0x16e8    20      FUNC    GLOBAL  0       8       restore_core_regs
  [  21] 0x0       0       FUNC    GLOBAL  0       UNDEF   memcpy  
  [  22] 0x1021    4       FUNC    GLOBAL  0       8       _Unwind_GetCFA
  [  23] 0x1025    78      FUNC    GLOBAL  0       8       __gnu_Unwind_RaiseException
  [  24] 0x1073    20      FUNC    GLOBAL  0       8       __gnu_Unwind_ForcedUnwind
  [  25] 0x1087    68      FUNC    GLOBAL  0       8       __gnu_Unwind_Resume
  [  26] 0x10cb    26      FUNC    GLOBAL  0       8       __gnu_Unwind_Resume_or_Rethrow
  [  27] 0x10e5    2       FUNC    GLOBAL  0       8       _Unwind_Complete
  [  28] 0x10e7    16      FUNC    GLOBAL  0       8       _Unwind_DeleteException
  [  29] 0x10f7    52      FUNC    GLOBAL  0       8       _Unwind_VRS_Get
  [  30] 0x1be9    18      FUNC    GLOBAL  0       8       __gnu_thumb1_case_uqi
  [  31] 0x1141    52      FUNC    GLOBAL  0       8       _Unwind_VRS_Set
  [  32] 0x118d    112     FUNC    GLOBAL  0       8       __gnu_Unwind_Backtrace
  [  33] 0x0       0       NOTYPE  WEAK    0       UNDEF   __cxa_begin_cleanup
  [  34] 0x0       0       NOTYPE  WEAK    0       UNDEF   __cxa_type_match
  [  35] 0x1909    656     FUNC    GLOBAL  0       8       __gnu_unwind_execute
  [  36] 0x0       0       NOTYPE  WEAK    0       UNDEF   __cxa_call_unexpected
  [  37] 0x149b    590     FUNC    GLOBAL  0       8       _Unwind_VRS_Pop
  [  38] 0x1770    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Save_WMMXD
  [  39] 0x17c8    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Save_WMMXC
  [  40] 0x1714    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Save_VFP_D
  [  41] 0x1704    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Save_VFP
  [  42] 0x1724    0       FUNC    GLOBAL  0       8       __gnu_Unwind_Save_VFP_D_16_to_31
  [  43] 0x16e8    20      FUNC    GLOBAL  0       8       __restore_core_regs
  [  44] 0x17dc    42      FUNC    GLOBAL  0       8       ___Unwind_RaiseException
  [  45] 0x17dc    42      FUNC    GLOBAL  0       8       _Unwind_RaiseException
  [  46] 0x1808    42      FUNC    GLOBAL  0       8       ___Unwind_Resume
  [  47] 0x1808    42      FUNC    GLOBAL  0       8       _Unwind_Resume
  [  48] 0x1834    42      FUNC    GLOBAL  0       8       ___Unwind_Resume_or_Rethrow
  [  49] 0x1834    42      FUNC    GLOBAL  0       8       _Unwind_Resume_or_Rethrow
  [  50] 0x1860    42      FUNC    GLOBAL  0       8       ___Unwind_ForcedUnwind
  [  51] 0x1860    42      FUNC    GLOBAL  0       8       _Unwind_ForcedUnwind
  [  52] 0x188c    42      FUNC    GLOBAL  0       8       ___Unwind_Backtrace
  [  53] 0x188c    42      FUNC    GLOBAL  0       8       _Unwind_Backtrace
  [  54] 0x1b99    38      FUNC    GLOBAL  0       8       __gnu_unwind_frame
  [  55] 0x1bbf    10      FUNC    GLOBAL  0       8       _Unwind_GetRegionStart
  [  56] 0x1bc9    20      FUNC    GLOBAL  0       8       _Unwind_GetLanguageSpecificData
  [  57] 0x1bdd    6       FUNC    GLOBAL  0       8       _Unwind_GetDataRelBase
  [  58] 0x1be3    6       FUNC    GLOBAL  0       8       _Unwind_GetTextRelBase
  [  59] 0x400c    0       NOTYPE  GLOBAL  0       ABS     _edata  
  [  60] 0x400c    0       NOTYPE  GLOBAL  0       ABS     __bss_start
  [  61] 0x4010    0       NOTYPE  GLOBAL  0       ABS     _end    

[+] Dynamic Link Table:
  #      Tag             Type            Name/Value
  [   0] 0x3             PLTGOT          0x3fd4          
  [   1] 0x2             PLTRELSZ        0x40            
  [   2] 0x17            JMPREL          0xc28           
  [   3] 0x14            PLTREL          0x11            
  [   4] 0x11            REL             0xbd8           
  [   5] 0x12            RELSZ           0x50            
  [   6] 0x13            RELENT          0x8             
  [   7] 0x6ffffffa      RELCOUNT        0x8             
  [   8] 0x6             SYMTAB          0x148           
  [   9] 0xb             SYMENT          0x10            
  [  10] 0x5             STRTAB          0x528           
  [  11] 0xa             STRSZ           0x51c           
  [  12] 0x4             HASH            0xa44           
  [  13] 0x1             NEEDED          Shared library: [liblog.so]
  [  14] 0x1             NEEDED          Shared library: [libstdc++.so]
  [  15] 0x1             NEEDED          Shared library: [libm.so]
  [  16] 0x1             NEEDED          Shared library: [libc.so]
  [  17] 0x1             NEEDED          Shared library: [libdl.so]
  [  18] 0xe             SONAME          Library soname: [libdemo1.so]
  [  19] 0x1a            FINIT_ARRAY     0x3ea4          
  [  20] 0x1c            FINIT_ARRAYSZ   0x8             
  [  21] 0x19            INIT_ARRAY      0x3eac          
  [  22] 0x1b            INIT_ARRAYSZ    0x4             
  [  23] 0x10            SYMBOLIC        0x0             
  [  24] 0x1e            FLAGS           0xa             
  [  25] 0x6ffffffb      FLAGS_1         0x1             
  [  26] 0x0             NULL            0x0             
  [  27] 0x0             NULL            0x0             
  [  28] 0x0             NULL            0x0             
  [  29] 0x0             NULL            0x0             
  [  30] 0x0             NULL            0x0             
  [  31] 0x0             NULL            0x0             


```
