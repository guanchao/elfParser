#!/usr/bin/env python
#coding:utf-8

import sys
import binascii


'''
# 节区类型定义
/* sh_type */
#define SHT_NULL	0
#define SHT_PROGBITS	1
#define SHT_SYMTAB	2
#define SHT_STRTAB	3
#define SHT_RELA	4
#define SHT_HASH	5
#define SHT_DYNAMIC	6
#define SHT_NOTE	7
#define SHT_NOBITS	8
#define SHT_REL	9
#define SHT_SHLIB	10
#define SHT_DYNSYM	11
#define SHT_NUM	12
#define SHT_LOPROC	0x70000000
#define SHT_HIPROC	0x7fffffff
#define SHT_LOUSER	0x80000000
#define SHT_HIUSER	0xffffffff
#define SHT_MIPS_LIST	0x70000000
#define SHT_MIPS_CONFLICT	0x70000002
#define SHT_MIPS_GPTAB	0x70000003
#define SHT_MIPS_UCODE	0x70000004
'''
SH_TYPE_MAP_LIST = {0:'SHT_NULL',
                    1:'SHT_PROGBITS',
                    2:'SHT_SYMTAB',
                    3:'SHT_STRTAB',
                    4:'SHT_RELA',
                    5:'SHT_HASH',
                    6:'SHT_DYNAMIC',
                    7:'SHT_NOTE',
                    8:'SHT_NOBITS',
                    9:'SHT_REL',
                    10:'SHT_SHLIB',
                    11:'SHT_DYNSYM',
                    # 0x60000000:'SHT_LOOS',
                    # 0x6fffffff:'SHT_HIOS',
                    0x70000000:'SHT_LOPROC',
                    0x7FFFFFFF:'SHT_HIPROC',
                    0x80000000:'SHT_LOUSER',
                    0x8FFFFFFF:'SHT_HIUSER',
                    0x70000000:'SHT_MIPS_LIST',
                    0x70000002:'SHT_MIPS_CONFLICT',
                    0x70000003:'SHT_MIPS_GPTAB',
                    0x70000004:'SHT_MIPS_UCODE',
                    }

PT_TYPE_MAP_LIST = {
    0:'NULL',
    1:'LOAD',
    2:'DYNAMIC',
    3:'INTERP',
    4:'NOTE',
    5:'SHLIB',
    6:'PHDR',
    7:'TLS',
    0x70000000:'LOPROC',
    0x70000001:'HIPROC',
    0x6474E551:'GNU_STACK',
    0x6474E552:'GNU_RELRO',
}

'''
Elf32_Dyn.d_tag
'''
DYNAMIC_TYPE = {
    0: 'NULL',
    1: 'NEEDED',
    2: 'PLTRELSZ',
    3: 'PLTGOT',
    4: 'HASH',
    5: 'STRTAB',
    6: 'SYMTAB',
    7: 'RELA',
    8: 'RELASZ',
    9: 'RELAENT',
    10: 'STRSZ',
    11: 'SYMENT',
    12: 'INIT',
    13: 'FINIT',
    14: 'SONAME',
    15: 'RPATH',
    16: 'SYMBOLIC',
    17: 'REL',
    18: 'RELSZ',
    19: 'RELENT',
    20: 'PLTREL',
    21: 'DEBUG',
    22: 'TEXTREL',
    23: 'JMPREL',
    26: 'FINIT_ARRAY',
    28: 'FINIT_ARRAYSZ',
    25: 'INIT_ARRAY',
    27: 'INIT_ARRAYSZ',
    30: 'FLAGS',
    0x6FFFFFFA: 'RELCOUNT',
    0x6FFFFFFB: 'FLAGS_1',
    0x70000000: 'LOPROC',
    0x7fffffff: 'HIPROC',
    0x70000001: 'MIPS_RLD_VERSION',
    0x70000002: 'MIPS_TIME_STAMP',
    0x70000003: 'MIPS_ICHECKSUM',
    0x70000004: 'MIPS_IVERSION',
    0x70000005: 'MIPS_FLAGS',
    0x70000006: 'MIPS_BASE_ADDRESS',
    0x70000008: 'MIPS_CONFLICT',
    0x70000009: 'MIPS_LIBLIST',
    0x7000000a: 'MIPS_LOCAL_GOTNO',
    0x7000000b: 'MIPS_CONFLICTNO',
    0x70000010: 'MIPS_LIBLISTNO',
    0x70000011: 'MIPS_SYMTABNO',
    0x70000012: 'MIPS_UNREFEXTNO',
    0x70000013: 'MIPS_GOTSYM',
    0x70000014: 'MIPS_HIPAGENO',
    0x70000016: 'MIPS_RLD_MAP',

}
'''
typedef struct elf32_hdr{
  unsigned char	e_ident[EI_NIDENT];
  Elf32_Half	e_type;
  Elf32_Half	e_machine;
  Elf32_Word	e_version;
  Elf32_Addr	e_entry;  /* Entry point */
  Elf32_Off	e_phoff;
  Elf32_Off	e_shoff;
  Elf32_Word	e_flags;
  Elf32_Half	e_ehsize;
  Elf32_Half	e_phentsize;
  Elf32_Half	e_phnum;
  Elf32_Half	e_shentsize;
  Elf32_Half	e_shnum;
  Elf32_Half	e_shstrndx;
} Elf32_Ehdr;
'''
class Elf32_Ehdr(object):
    """docstring for Elf32_Ehdr"""
    def __init__(self):
        super(Elf32_Ehdr, self).__init__()
        self.e_ident = None
        self.e_type = None
        self.e_machine = None
        self.e_version = None
        self.e_entry = None
        self.e_phoff = None
        self.e_shoff = None
        self.e_flags = None
        self.e_ehsize = None
        self.e_phentsize = None
        self.e_phnum = None
        self.e_shentsize = None
        self.e_shnum = None
        self.e_shstrndx = None

class e_ident(object):
    """docstring for e_ident"""
    def __init__(self):
        super(e_ident, self).__init__()
        self.file_identification = None
        self.ei_class = None
        self.ei_data = None
        self.ei_version = None
        self.ei_osabi = None
        self.ei_abiversion = None
        self.ei_pad = None
        self.ei_nident = None

    def __str__(self):
        return 'e_ident=[file_identification=%s, ei_class=%d, ei_data=%d, ei_version=%d, ei_osabi=%d, ei_abiversion=%d, ei_pad=%s, ei_nident=%d]' % (
        self.file_identification, self.ei_class, self.ei_data, self.ei_version, self.ei_osabi, self.ei_abiversion, self.ei_pad, self.ei_nident)

class Elf32_Shdr(object):
    """docstring for Elf32_Shdr"""
    def __init__(self):
        super(Elf32_Shdr, self).__init__()
        '''
        typedef struct Elf32_Shdr {
          Elf32_Word	sh_name;
          Elf32_Word	sh_type;
          Elf32_Word	sh_flags;
          Elf32_Addr	sh_addr;
          Elf32_Off	sh_offset;
          Elf32_Word	sh_size;
          Elf32_Word	sh_link;
          Elf32_Word	sh_info;
          Elf32_Word	sh_addralign;
          Elf32_Word	sh_entsize;
        } Elf32_Shdr;
        '''
        self.sh_name = None
        self.sh_type = None
        self.sh_flags = None
        self.sh_addr = None
        self.sh_offset = None
        self.size = None
        self.sh_link = None
        self.sh_addralign = None
        self.sh_entsize = None

        self.section_name = None

    def __str__(self):
        return 'Elf32_Shdr=[sh_name=%s, sh_type=%d, sh_flags=%d, sh_addr=%s, sh_sh_offset=%s, sh_size=%d, sh_link=%d, sh_info=%d, sh_addralign=%d, sh_entsize=%d]' % \
               (hex(self.sh_name), self.sh_type, self.sh_flags, hex(self.sh_addr), hex(self.sh_offset), self.sh_size, self.sh_link, self.sh_info, self.sh_addralign, self.sh_entsize)

class Elf32_Sym(object):
    """docstring for Elf32_Sym"""
    def __init__(self):
        super(Elf32_Sym, self).__init__()
        '''
        typedef struct elf32_sym{
          Elf32_Word	st_name;
          Elf32_Addr	st_value;
          Elf32_Word	st_size;
          unsigned char	st_info;
          unsigned char	st_other;
          Elf32_Half	st_shndx;
        } Elf32_Sym;
        '''
        self.st_name = None
        self.st_value = None
        self.st_size = None
        self.st_info = None
        self.st_other = None
        self.st_shndx = None

        self.symbol_name = None

    def __str__(self):
        return 'Elf32_Dyn=[st_name=%s, st_value=%d, st_size=%d, st_info=%d, st_other=%d, st_shndx=%d] #%s' % \
               (self.st_name, self.st_value, self.st_size, self.st_info, self.st_other, self.st_shndx, self.symbol_name)


class Elf32_Phdr(object):
    """docstring for Elf32_Phdr"""
    def __init__(self):
        super(Elf32_Phdr, self).__init__()
        '''
            /* 32-bit ELF base types. */
            typedef uint32_t Elf32_Addr;
            typedef uint16_t Elf32_Half;
            typedef uint32_t Elf32_Off;
            typedef int32_t  Elf32_Sword;
            typedef uint32_t Elf32_Word;
        '''
        self.p_type = None # Elf32_Word
        self.p_offset = None # Elf32_Off
        self.p_vaddr = None # Elf32_Addr
        self.p_paddr = None # Elf32_Addr
        self.p_filesz = None # Elf32_word
        self.p_memsz = None # Elf32_Word
        self.p_flags = None # Elf32_Word
        self.p_align = None # Elf32_Word

class Elf32_Dyn(object):
    """docstring for Elf32_dyn"""
    def __init__(self):
        super(Elf32_Dyn, self).__init__()
        '''
        typedef struct dynamic{
          Elf32_Sword d_tag;
          union{
            Elf32_Sword	d_val;
            Elf32_Addr	d_ptr;
          } d_un;
        } Elf32_Dyn;
        '''
        self.d_tag = None
        self.d_un = None

    def __str__(self):
        return 'Elf32_Dyn=[d_tag=%d, d_un=%d]' % \
               (self.d_tag, self.d_un)


class ELF(object):
    """docstring for ELF"""
    def __init__(self, filepath):
        super(ELF, self).__init__()
        self.filepath = filepath
        self.elf32_Ehdr = Elf32_Ehdr()

        # section header table
        self.sectionHeaderTable = []

        # section name table
        self.sectionNameTable = None

        # program header table
        self.programHeaderTable = []

        # dynamic symbol table
        self.symbolTable = []  # .dynsym
        self.dynstrTable = None # .dynstr

        # dynamic link table
        self.dynamicLinkTable = [] # .dynamic

        self.initELFHeader()
        self.initSectionHeader()
        self.initProgramHeader()
        self.initSymbolTalbe()
        self.initDynamicLinkTable()


    def initELFHeader(self):
        f = open(self.filepath, "rb")
        self.f = f
        # unsigned char	e_ident[EI_NIDENT];
        f.seek(0, 0)
        self.elf32_Ehdr.e_ident = e_ident()
        self.elf32_Ehdr.e_ident.file_identification = f.read(4)
        self.elf32_Ehdr.e_ident.ei_class = int(binascii.b2a_hex(f.read(1)), 16)
        self.elf32_Ehdr.e_ident.ei_data = int(binascii.b2a_hex(f.read(1)), 16)
        self.elf32_Ehdr.e_ident.ei_version = int(binascii.b2a_hex(f.read(1)), 16)
        self.elf32_Ehdr.e_ident.ei_osabi = int(binascii.b2a_hex(f.read(1)), 16)
        self.elf32_Ehdr.e_ident.ei_abiversion = int(binascii.b2a_hex(f.read(1)), 16)
        self.elf32_Ehdr.e_ident.ei_pad = binascii.b2a_hex(f.read(6))
        self.elf32_Ehdr.e_ident.ei_nident = int(binascii.b2a_hex(f.read(1)), 16)

        # Elf32_Half	e_type;
        f.seek(16, 0)
        self.elf32_Ehdr.e_type = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_machine;
        f.seek(18, 0)
        self.elf32_Ehdr.e_machine = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Word	e_version;
        f.seek(20, 0)
        self.elf32_Ehdr.e_version = int(binascii.b2a_hex(f.read(4)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Addr	e_entry;
        f.seek(24, 0)
        self.elf32_Ehdr.e_entry = int(binascii.b2a_hex(f.read(4)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Off	e_phoff;
        f.seek(28, 0)
        self.elf32_Ehdr.e_phoff = int(binascii.b2a_hex(f.read(4)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Off	e_shoff;
        f.seek(32, 0)
        self.elf32_Ehdr.e_shoff = int(binascii.b2a_hex(f.read(4)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Word	e_flags;
        f.seek(36, 0)
        self.elf32_Ehdr.e_flags = int(binascii.b2a_hex(f.read(4)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_ehsize;
        f.seek(40, 0)
        self.elf32_Ehdr.e_ehsize = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_phentsize;
        f.seek(42, 0)
        self.elf32_Ehdr.e_phentsize = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_phnum;
        f.seek(44, 0)
        self.elf32_Ehdr.e_phnum = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_shentsize;
        f.seek(46, 0)
        self.elf32_Ehdr.e_shentsize = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_shnum;
        f.seek(48, 0)
        self.elf32_Ehdr.e_shnum = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

        # Elf32_Half	e_shstrndx;
        f.seek(50, 0)
        self.elf32_Ehdr.e_shstrndx = int(binascii.b2a_hex(f.read(2)).decode('hex')[::-1].encode('hex'), 16)

    def initSectionHeader(self):
        for i in range(self.elf32_Ehdr.e_shnum):
            self.sectionHeaderTable.append(self.parseSectionHeader(self.elf32_Ehdr.e_shoff + i * self.elf32_Ehdr.e_shentsize))

        if self.elf32_Ehdr.e_shnum == 0:
            return
        # init section name table
        self.f.seek(self.sectionHeaderTable[self.elf32_Ehdr.e_shstrndx].sh_offset)
        size = self.sectionHeaderTable[self.elf32_Ehdr.e_shstrndx].sh_size
        self.sectionNameTable = self.f.read(size)

        for i in xrange(self.elf32_Ehdr.e_shnum):
            idx = self.sectionHeaderTable[i].sh_name
            name = []
            while True:
                if self.sectionNameTable[idx] != '\0':
                    name.append(self.sectionNameTable[idx])
                else:
                    break
                idx += 1
            self.sectionHeaderTable[i].section_name = "".join(name)

    def parseSectionHeader(self, offset):
        self.f.seek(offset, 0)
        elf32_Shdr = Elf32_Shdr()
        elf32_Shdr.sh_name = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_type = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_flags = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_addr = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_offset = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_size = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_link = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_info = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_addralign = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Shdr.sh_entsize = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        return elf32_Shdr

    def displaySectionHeader(self):
        print '[+] Section Header Table:'
        print '  #      %-32s%-16s%-16s%-16s%-8s%-8s%-8s%-8s%-8s%-8s' % ('Name', 'Type', 'Addr', 'Offset', 'Size', 'ES', 'Flg', 'Lk', 'Inf', 'Al')
        for index in range(len(self.sectionHeaderTable)):
            elf32_Shdr = self.sectionHeaderTable[index]
            if elf32_Shdr.sh_type in SH_TYPE_MAP_LIST:
                print '  [%4d] %-32s%-16s%-16s%-16s%-8s%-8d%-8d%-8d%-8d%-8d' % \
                      (index,
                       self.getSectionName(elf32_Shdr),
                       SH_TYPE_MAP_LIST[elf32_Shdr.sh_type].strip(),
                       hex(elf32_Shdr.sh_addr),
                       hex(elf32_Shdr.sh_offset),
                       hex(elf32_Shdr.sh_size),
                       elf32_Shdr.sh_entsize,
                       elf32_Shdr.sh_flags,
                       elf32_Shdr.sh_link,
                       elf32_Shdr.sh_info,
                       elf32_Shdr.sh_addralign,
                       )
            else:
                print '  [%4d] %-32s%-16d%-16s%-16s%-8s%-8d%-8d%-8d%-8d%-8d' % \
                      (index,
                       self.getSectionName(elf32_Shdr),
                       elf32_Shdr.sh_type,
                       hex(elf32_Shdr.sh_addr),
                       hex(elf32_Shdr.sh_offset),
                       hex(elf32_Shdr.sh_size),
                       elf32_Shdr.sh_entsize,
                       elf32_Shdr.sh_flags,
                       elf32_Shdr.sh_link,
                       elf32_Shdr.sh_info,
                       elf32_Shdr.sh_addralign,
                       )
        print ''

    def getSectionName(self, elf32_Shdr):
        idx = self.sectionNameTable.find('\0', elf32_Shdr.sh_name)
        return self.sectionNameTable[elf32_Shdr.sh_name:idx]

    def initProgramHeader(self):
        for i in range(self.elf32_Ehdr.e_phnum):
            self.programHeaderTable.append(self.parseProgramHeader(self.elf32_Ehdr.e_phoff + i * self.elf32_Ehdr.e_phentsize))

    def parseProgramHeader(self, offset):
        '''
        typedef struct elf32_phdr{
          Elf32_Word	p_type;
          Elf32_Off	p_offset;
          Elf32_Addr	p_vaddr;
          Elf32_Addr	p_paddr;
          Elf32_Word	p_filesz;
          Elf32_Word	p_memsz;
          Elf32_Word	p_flags;
          Elf32_Word	p_align;
        } Elf32_Phdr;
        '''
        self.f.seek(offset, 0)
        elf32_Phdr = Elf32_Phdr()
        elf32_Phdr.p_type = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_offset = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_vaddr = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_paddr = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_filesz = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_memsz = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_flags = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Phdr.p_align = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        return elf32_Phdr

    def displayProgramHeader(self):
        print '[+] Program Header Table:'
        print '  #      %-16s%-16s%-16s%-16s%-8s%-8s%-8s%-8s' % (
            'Type', 'offset', 'VirtAddr', 'PhysAddr', 'FileSiz', 'MemSiz', 'Flg', 'Align')
        for index in range(len(self.programHeaderTable)):
            elf32_Phdr = self.programHeaderTable[index]

            if elf32_Phdr.p_type in PT_TYPE_MAP_LIST:
                print '  [%4d] %-16s%-16s%-16s%-16s%-8s%-8s%-8d%-8s' % (
                    index,
                    PT_TYPE_MAP_LIST[elf32_Phdr.p_type],
                    hex(elf32_Phdr.p_offset),
                    hex(elf32_Phdr.p_vaddr),
                    hex(elf32_Phdr.p_paddr),
                    hex(elf32_Phdr.p_filesz),
                    hex(elf32_Phdr.p_memsz),
                    elf32_Phdr.p_flags,
                    hex(elf32_Phdr.p_align),
                )
            else:
                print '  [%4d] %-16d%-16s%-16s%-16s%-8s%-8s%-8d%-8s' % (
                    index,
                    elf32_Phdr.p_type,
                    hex(elf32_Phdr.p_offset),
                    hex(elf32_Phdr.p_vaddr),
                    hex(elf32_Phdr.p_paddr),
                    hex(elf32_Phdr.p_filesz),
                    hex(elf32_Phdr.p_memsz),
                    elf32_Phdr.p_flags,
                    hex(elf32_Phdr.p_align),
                )
        print '\n[+] Section to segment mapping:'
        for index in range(len(self.programHeaderTable)):
            elf32_Phdr = self.programHeaderTable[index]
            sections = self.getSegmentSections(elf32_Phdr)

            sections_str = ''
            for elf32_Shdr in sections:
                idx = self.sectionNameTable.index('\0', elf32_Shdr.sh_name)
                sections_str += self.sectionNameTable[elf32_Shdr.sh_name:idx] + ' '
            print '  [%4d] %s' % (index, sections_str)
        print ''

    def getSegmentSections(self, elf32_Phdr):
        start = elf32_Phdr.p_offset
        end = elf32_Phdr.p_offset + elf32_Phdr.p_filesz

        sections = []
        for index in range(len(self.sectionHeaderTable)):
            elf32_Shdr = self.sectionHeaderTable[index]
            section_start = elf32_Shdr.sh_offset
            section_end = elf32_Shdr.sh_offset + elf32_Shdr.sh_size
            if section_start >= start and section_end <= end:
                sections.append(elf32_Shdr)

        return sections


    def initSymbolTalbe(self):
        # init dynsym
        elf32_Shdr = self.getSectionByName('.dynsym')
        if elf32_Shdr != None:
            for i in range(elf32_Shdr.sh_size / elf32_Shdr.sh_entsize):
                self.symbolTable.append(self.parseSymbolTable(elf32_Shdr.sh_offset + i * elf32_Shdr.sh_entsize))

        # init dynstr
        dynstr_elf32_Shdr = self.getSectionByName('.dynstr')
        self.f.seek(dynstr_elf32_Shdr.sh_offset)

        self.dynstrTable = self.f.read(dynstr_elf32_Shdr.sh_size)

        for i in range(len(self.symbolTable)):
            idx = self.symbolTable[i].st_name
            name = []
            while True:
                if self.dynstrTable[idx] != '\0':
                    name.append(self.dynstrTable[idx])
                else:
                    break
                idx += 1
            self.symbolTable[i].symbol_name = "".join(name)

    def parseSymbolTable(self, offset):
        '''
            typedef struct elf32_sym{
              Elf32_Word	st_name;
              Elf32_Addr	st_value;
              Elf32_Word	st_size;
              unsigned char	st_info;
              unsigned char	st_other;
              Elf32_Half	st_shndx;
            } Elf32_Sym;
        '''
        self.f.seek(offset, 0)
        elf32_Sym = Elf32_Sym()
        elf32_Sym.st_name = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Sym.st_value = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Sym.st_size = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Sym.st_info = int(binascii.b2a_hex(self.f.read(1)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Sym.st_other = int(binascii.b2a_hex(self.f.read(1)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Sym.st_shndx = int(binascii.b2a_hex(self.f.read(2)).decode('hex')[::-1].encode('hex'), 16)
        return elf32_Sym

    def displaySymbolTable(self):
        print '[+] Dynamic Symbol Table:'
        print '  #      %-10s%-8s%-8s%-8s%-8s%-8s%-8s' % (
            'Value', 'Size', 'Type', 'Bind', 'Other', 'Ndx', 'Name')

        BIND_TYPE = {0:'LOCAL', 1:'GLOBAL', 2:'WEAK', 13:'LOPROC', 15:'HIPROC'}
        ELF32_ST_TYPE = {0:'NOTYPE', 1:'OBJECT', 2:'FUNC', 3:'SECTION', 4:'FILE', 13:'LOPROC', 15:'HIPROC'}
        SHN_TYPE = {0:'UNDEF', 0xfff1:'ABS',  0xfff2:'COMMON',}

        for index in range(len(self.symbolTable)):
            elf32_Sym = self.symbolTable[index]
            bind = elf32_Sym.st_info >> 4
            type = elf32_Sym.st_info & 0xf

            if elf32_Sym.st_shndx == 0 or elf32_Sym.st_shndx == 0xfff1 or elf32_Sym.st_shndx == 0xfff2:
                shn_type = SHN_TYPE[elf32_Sym.st_shndx]
            else:
                shn_type = str(elf32_Sym.st_shndx)
            print '  [%4d] %-10s%-8d%-8s%-8s%-8d%-8s%-8s' % (
                index,
                hex(elf32_Sym.st_value),
                elf32_Sym.st_size,
                ELF32_ST_TYPE[type],
                BIND_TYPE[bind],
                elf32_Sym.st_other,
                shn_type,
                elf32_Sym.symbol_name
            )
        print ''

    def initDynamicLinkTable(self):
        # init dynamic
        elf32_Shdr = self.getSectionByName('.dynamic')
        if elf32_Shdr != None:
            for i in range(elf32_Shdr.sh_size / elf32_Shdr.sh_entsize):
                self.dynamicLinkTable.append(self.parseDynamicLinkTable(elf32_Shdr.sh_offset + i * elf32_Shdr.sh_entsize))

    def parseDynamicLinkTable(self, offset):
        '''
        typedef struct dynamic{
          Elf32_Sword d_tag;
          union{
            Elf32_Sword	d_val;
            Elf32_Addr	d_ptr;
          } d_un;
        } Elf32_Dyn;
        '''
        self.f.seek(offset, 0)
        elf32_Dyn = Elf32_Dyn()
        elf32_Dyn.d_tag = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        elf32_Dyn.d_un = int(binascii.b2a_hex(self.f.read(4)).decode('hex')[::-1].encode('hex'), 16)
        return elf32_Dyn

    def displayDynamicLinkTable(self):
        print '[+] Dynamic Link Table:'
        print '  #      %-16s%-16s%-8s' % ('Tag', 'Type', 'Name/Value')

        for index in range(len(self.dynamicLinkTable)):
            elf32_Dyn = self.dynamicLinkTable[index]
            print '  [%4d] %-16s%-16s%-16s' % (
                index,
                hex(elf32_Dyn.d_tag),
                DYNAMIC_TYPE[elf32_Dyn.d_tag],
                self.getElf32_Dyn_TypeInfo(elf32_Dyn),

            )

    def getElf32_Dyn_TypeInfo(self, elf32_Dyn):
        if elf32_Dyn.d_tag == 1: # DT_NEEDED
            idx = self.dynstrTable.find('\0', elf32_Dyn.d_un)
            return 'Shared library: [%s]' % self.dynstrTable[elf32_Dyn.d_un: idx]

        elif elf32_Dyn.d_tag == 0xe: # DT_SONAME
            idx = self.dynstrTable.find('\0', elf32_Dyn.d_un)
            return 'Library soname: [%s]' % self.dynstrTable[elf32_Dyn.d_un: idx]

        return hex(elf32_Dyn.d_un)

    def displayELFHeader(self):
        print '[+] ELF Header:'
        print 'e_ident:\t%s' % self.elf32_Ehdr.e_ident
        print 'e_type: \t%s' % self.elf32_Ehdr.e_type
        print 'e_machine:\t%s' % self.elf32_Ehdr.e_machine
        print 'e_version:\t%s' % self.elf32_Ehdr.e_version
        print 'e_entry:\t%s' % self.elf32_Ehdr.e_entry
        print 'e_phoff:\t%s\t//Program header offset' % hex(self.elf32_Ehdr.e_phoff)
        print 'e_shoff:\t%s\t//Section header offset' % hex(self.elf32_Ehdr.e_shoff)
        print 'e_flags:\t%s' % self.elf32_Ehdr.e_flags
        print 'e_ehsize:\t%s\t//ELF header size' % self.elf32_Ehdr.e_ehsize
        print 'e_phentsize:\t%s\t//Program header entry size' % self.elf32_Ehdr.e_phentsize
        print 'e_phnum:\t%s\t//Program header number' % self.elf32_Ehdr.e_phnum
        print 'e_shentsize:\t%s\t//Section header entry size' % self.elf32_Ehdr.e_shentsize
        print 'e_shnum:\t%s\t//Section header number' % self.elf32_Ehdr.e_shnum
        print 'e_shstrndx:\t%s\t//Section header string index' % self.elf32_Ehdr.e_shstrndx
        print ''

    def disassemble(self):
        '''
        Display assembler contents of executable sections (.text .plt ...)
        '''
        self.__disassembleTEXTSection()
        self.__disassemblePLTSection()

    def __disassembleTEXTSection(self):
        elf32_Shdr = self.getSectionByName('.text')
        if elf32_Shdr == None:
            return
        # TODO
        pass

    def __disassemblePLTSection(self):
        elf32_Shdr = self.getSectionByName('.plt')
        if elf32_Shdr == None:
            return
        # TODO
        pass

    def getSectionByName(self, name):
        for elf32_Shdr in self.sectionHeaderTable:
            if elf32_Shdr.section_name == name:
                return elf32_Shdr
        return None

if __name__ == '__main__':
    elf = ELF(sys.argv[1])
    elf.displayELFHeader()
    elf.displaySectionHeader()
    elf.displayProgramHeader()
    elf.displaySymbolTable()
    elf.displayDynamicLinkTable()
    elf.disassemble()



