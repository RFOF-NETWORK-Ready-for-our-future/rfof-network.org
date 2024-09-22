TOKEN = os.getenv("6774549752:AAFx5D-reu3Pu-qkmKLh2aNxumv4faZtRN0") ("6774549752:AAFx5D-reu3Pu-qkmKLh2aNxumv4faZtRN0")

f"Total Supply: 999999999999999999999999900\n"
        f"Mintable: true\n"
        f"Admin Address: 0:e4fb51aa7386080b6d8b4c00192f1a26864ca9f95e76074c9a787826937b7d2e\n"
        f"Master Address: EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D\n"
        f"Wallet Address: EQC_LhrYP8fvFgtDLEhrWnuSLo8w4cCI4o-CFSIGOCOTmwjj\n"
        f"Holder Address: EQDYMcZf6OAdtvhJma887wHdyH_dowjYWoiOf9zy5Mm5-q8D\n"
        f"Hey Hash: 8da55a166c83c8cea677f2fbb4925ef81eda782cee73bacaa82d5c4e87882138\n"
        f"Jetton Content: Contains metadata of the token, such as the name and description.\n"
        f"Jetton Wallet Code: SETCP0
(:methods
  recv_internal: 
    s0 s1 XCHG
    CTOS
    4 LDU
    s0 s1 XCHG
    1 PUSHINT
    AND
    NEGATE
    s0 s1 XCHG
    LDMSGADDR
    s0 s1 XCHG
    s0 PUSH
    SBITS
    267 PUSHINT
    EQUAL
    136 THROWIFNOT
    s0 PUSH
    11 PLDU
    s0 PUSH
    1279 PUSHINT
    EQUAL
    137 THROWIF
    10 PUSHPOW2
    EQUAL
    136 THROWIFNOT
    0 4 2 PUXCPU
    s0 s3 XCHG
    4 TUPLE
    1 SETGLOBVAR
    s0 s2 XCHG
    2 SETGLOBVAR
    <{
      c4 PUSH
      CTOS
      LDREF
      s0 s1 XCHG
      3 SETGLOBVAR
      1 LDI
      s0 s1 XCHG
      <{
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDREF
        1 LDI
        64 LDU
        5 1 BLKSWAP
        1 5 BLKDROP2
      }> PUSHCONT
      IFJMP
      MYADDR
      11 PLDU
      10 PUSHPOW2
      EQUAL
      137 THROWIFNOT
      LDMSGADDR
      s0 s1 XCHG
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
      s0 s1 XCHG
      257 PUSHINT
      LDI
      LDREF
      3 1 BLKSWAP
      s0 s3 XCHG
      ENDS
      ROT
      <{
        -1 PUSHINT
        0 PUSHINT
        s0 s4 XCHG
        s0 s3 XCHG
      }> CALLREF
    }> CALLREF
    2 5 BLKSWAP
    <{
      c2 SAVE
      SAMEALTSAVE
      s0 s1 XCHG
      <{
        s0 POP
        -1 PUSHINT
      }> PUSHCONT
      IFJMP
      0 PUSHINT
      s1 PUSH
      SBITS
      31 GTINT
      <{
        s0 POP
        s0 PUSH
        32 PLDU
      }> PUSHCONT
      IF
      s0 PUSH
      0 EQINT
      s2 PUSH
      SBITS
      33 LESSINT
      AND
      <{
        2DROP
        -1 PUSHINT
      }> PUSHCONT
      IFJMP
      s0 PUSH
      1475151734 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        1475151734 PUSHINT
        EQUAL
        129 THROWIFNOT
        64 LDU
        257 PUSHINT
        LDI
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s3 s3 s0 XCHG3
        1 3 BLKDROP2
        s2 POP
        1 GETGLOBVAR
        4 UNTUPLE
        s2 s3 XCHG
        3 BLKDROP
        s6 PUSH
        14534 PUSHINT
        s0 s2 XCHG
        SDEQ
        THROWANYIFNOT
        3688 PUSHINT
        s4 PUSH
        THROWANYIFNOT
        s1 s6 XCHG
        s1 s5 XCHG
        s1 s4 XCHG
        s3 s3 s0 XCHG3
        6 -1 0 PUXCPU
        <{
          18668 PUSHINT
          s5 PUSH
          THROWANYIFNOT
          s7 s1 XCPU
          ADD
          5 2 BLKSWAP
          <{
            3 GETGLOBVAR
            MYADDR
            s1 s2 XCHG
            <{
              s0 s2 XCHG
              CTOS
              LDDICT
              s0 POP
              PUSHNULL
              s0 s1 XCHG
              55471 PUSHINT
              s0 s1 XCHG
              16 PUSHINT
              DICTUGETREF
              NULLSWAPIFNOT
              135 THROWIFNOT
              s0 s1 XCHG
              55471 PUSHINT
              s2 PUSH
              s0 s2 XCHG
              16 PUSHINT
              DICTUSETREF
              NEWC
              s0 s1 XCHG
              NEWC
              STDICT
              ENDC
              s0 s1 XCHG
              STREF
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s0 s3 XCHG3
              ROTREV
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              s0 s1 XCHG
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              ENDC
            }> CALLREF
          }> CALLREF
          2DUP
          0 PUSHINT
          ROTREV
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          2 STU
          3 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          STREF
          STREF
          ENDC
          HASHCU
          NEWC
          2 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          8 STI
          256 STU
          ENDC
          CTOS
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          0 PUSHINT
          -1 PUSHINT
          64 PUSHINT
          s2 PUSH
          MYADDR
          s1 PUSH
          NEWC
          ENDC
          CTOS
          s3 s5 XCHG
          s4 s15 XCHG
          s2 s3 XCHG
          s0 s2 XCHG
          s0 s16 XCHG
          s0 s2 XCHG
          NEWC
          6 1 BLKSWAP
          <{
            395134233 PUSHINT
            s0 s7 XCHG2
            32 STU
            s1 s5 XCHG
            64 STU
            s0 s3 XCHG2
            STGRAMS
            s0 s1 XCHG
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s1 XCHG
            s0 PUSH
            ISNULL
            <{
              s0 POP
              0 PUSHINT
              s0 s1 XCHG
              2 STU
            }> PUSHCONT
            <{
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
            }> PUSHCONT
            IFELSE
            s0 s1 XCHG
            STGRAMS
            s0 s1 XCHG
            STSLICER
          }> CALLREF
          ENDC
          s6 s5 s0 XCHG3
          s4 s11 XCHG
          s3 s10 XCHG
          s0 s11 s10 XCHG3
          s4 s6 XCHG
          s4 s5 XCHG
          <{
            NEWC
            1 PUSHINT
            s0 s1 XCHG
            2 STI
            s0 s7 XCHG2
            s0 s1 XCHG
            1 STI
            0 PUSHINT
            s0 s1 XCHG
            3 STI
            s0 s5 XCHG2
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s3 XCHG2
            STGRAMS
            0 PUSHINT
            s0 s1 XCHG
            105 STI
            s3 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
            }> PUSHCONT
            <{
              s4 PUSH
              ISNULL
              NOT
            }> PUSHCONT
            IFELSE
            <{
              s3 POP
              s3 POP
              s0 s1 XCHG
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              NEWC
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              ENDC
              ROT
              STREF
            }> IFREFELSE
            s1 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s1 XCHG
              s0 PUSH
              ISNULL
              128 THROWIF
              s0 s1 XCHG
              STREF
            }> PUSHCONT
            <{
              s1 POP
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            IFELSE
            ENDC
            s0 s1 XCHG
            SENDRAWMSG
          }> CALLREF
          s0 s3 s4 XCHG3
        }> CALLREF
        s3 POP
        s3 s4 XCHG
        ROT
        -1 PUSHINT
      }> IFJMPREF
      s0 PUSH
      3554595857 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        3554595857 PUSHINT
        EQUAL
        129 THROWIFNOT
        64 LDU
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s1 s2 XCHG
        1 2 BLKDROP2
        s1 POP
        1 GETGLOBVAR
        4 UNTUPLE
        s2 s3 XCHG
        3 BLKDROP
        s0 s5 XCHG
        14534 PUSHINT
        s0 s6 XCHG
        SDEQ
        s1 s5 XCHG
        THROWANYIFNOT
        -1 PUSHINT
      }> IFJMPREF
      s0 PUSH
      4235234258 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        4235234258 PUSHINT
        EQUAL
        129 THROWIFNOT
        257 PUSHINT
        LDI
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s1 s2 XCHG
        1 2 BLKDROP2
        1 GETGLOBVAR
        4 UNTUPLE
        s2 s3 XCHG
        3 BLKDROP
        s6 PUSH
        14534 PUSHINT
        s0 s2 XCHG
        SDEQ
        THROWANYIFNOT
        3688 PUSHINT
        s4 PUSH
        THROWANYIFNOT
        s1 s5 XCPU
        <{
          18668 PUSHINT
          s5 PUSH
          THROWANYIFNOT
          s7 s1 XCPU
          ADD
          5 2 BLKSWAP
          <{
            3 GETGLOBVAR
            MYADDR
            s1 s2 XCHG
            <{
              s0 s2 XCHG
              CTOS
              LDDICT
              s0 POP
              PUSHNULL
              s0 s1 XCHG
              55471 PUSHINT
              s0 s1 XCHG
              16 PUSHINT
              DICTUGETREF
              NULLSWAPIFNOT
              135 THROWIFNOT
              s0 s1 XCHG
              55471 PUSHINT
              s2 PUSH
              s0 s2 XCHG
              16 PUSHINT
              DICTUSETREF
              NEWC
              s0 s1 XCHG
              NEWC
              STDICT
              ENDC
              s0 s1 XCHG
              STREF
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s0 s3 XCHG3
              ROTREV
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              s0 s1 XCHG
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              ENDC
            }> CALLREF
          }> CALLREF
          2DUP
          0 PUSHINT
          ROTREV
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          2 STU
          3 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          STREF
          STREF
          ENDC
          HASHCU
          NEWC
          2 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          8 STI
          256 STU
          ENDC
          CTOS
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          0 PUSHINT
          -1 PUSHINT
          64 PUSHINT
          s2 PUSH
          MYADDR
          s1 PUSH
          NEWC
          ENDC
          CTOS
          s3 s5 XCHG
          s4 s15 XCHG
          s2 s3 XCHG
          s0 s2 XCHG
          s0 s16 XCHG
          s0 s2 XCHG
          NEWC
          6 1 BLKSWAP
          <{
            395134233 PUSHINT
            s0 s7 XCHG2
            32 STU
            s1 s5 XCHG
            64 STU
            s0 s3 XCHG2
            STGRAMS
            s0 s1 XCHG
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s1 XCHG
            s0 PUSH
            ISNULL
            <{
              s0 POP
              0 PUSHINT
              s0 s1 XCHG
              2 STU
            }> PUSHCONT
            <{
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
            }> PUSHCONT
            IFELSE
            s0 s1 XCHG
            STGRAMS
            s0 s1 XCHG
            STSLICER
          }> CALLREF
          ENDC
          s6 s5 s0 XCHG3
          s4 s11 XCHG
          s3 s10 XCHG
          s0 s11 s10 XCHG3
          s4 s6 XCHG
          s4 s5 XCHG
          <{
            NEWC
            1 PUSHINT
            s0 s1 XCHG
            2 STI
            s0 s7 XCHG2
            s0 s1 XCHG
            1 STI
            0 PUSHINT
            s0 s1 XCHG
            3 STI
            s0 s5 XCHG2
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s3 XCHG2
            STGRAMS
            0 PUSHINT
            s0 s1 XCHG
            105 STI
            s3 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
            }> PUSHCONT
            <{
              s4 PUSH
              ISNULL
              NOT
            }> PUSHCONT
            IFELSE
            <{
              s3 POP
              s3 POP
              s0 s1 XCHG
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              NEWC
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              ENDC
              ROT
              STREF
            }> IFREFELSE
            s1 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s1 XCHG
              s0 PUSH
              ISNULL
              128 THROWIF
              s0 s1 XCHG
              STREF
            }> PUSHCONT
            <{
              s1 POP
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            IFELSE
            ENDC
            s0 s1 XCHG
            SENDRAWMSG
          }> CALLREF
          s0 s3 s4 XCHG3
        }> CALLREF
        -1 PUSHINT
      }> IFJMPREF
      s0 PUSH
      2937889386 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        2937889386 PUSHINT
        EQUAL
        129 THROWIFNOT
        LDREF
        s0 s1 XCHG
        s1 POP
        5 1 BLKSWAP
        <{
          2 GETGLOBVAR
          s4 s-1 PUXC
          SDEQ
          132 THROWIFNOT
        }> CALLREF
        s2 POP
        s3 s4 XCHG
        s3 s0 s0 XCHG3
        -1 PUSHINT
      }> PUSHCONT
      IFJMP
      s0 PUSH
      2078119902 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        2078119902 PUSHINT
        EQUAL
        129 THROWIFNOT
        64 LDU
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDMSGADDR
        s1 PUSH
        2 PLDU
        0 NEQINT
        <{
          s0 s1 XCHG
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
        }> PUSHCONT
        <{
          s1 POP
          PUSHNULL
        }> PUSHCONT
        IFELSE
        s1 s4 XCHG
        s3 s3 s0 XCHG3
        1 4 BLKDROP2
        s1 POP
        s0 PUSH
        s0 PUSH
        ISNULL
        128 THROWIF
        s5 s8 XCHG
        s4 s7 XCHG
        s3 s6 XCHG
        s8 s7 s0 XCHG3
        <{
          1 GETGLOBVAR
          4 UNTUPLE
          s2 s3 XCHG
          3 BLKDROP
          6 1 BLKSWAP
          <{
            3 GETGLOBVAR
            MYADDR
            s1 s2 XCHG
            <{
              s0 s2 XCHG
              CTOS
              LDDICT
              s0 POP
              PUSHNULL
              s0 s1 XCHG
              55471 PUSHINT
              s0 s1 XCHG
              16 PUSHINT
              DICTUGETREF
              NULLSWAPIFNOT
              135 THROWIFNOT
              s0 s1 XCHG
              55471 PUSHINT
              s2 PUSH
              s0 s2 XCHG
              16 PUSHINT
              DICTUSETREF
              NEWC
              s0 s1 XCHG
              NEWC
              STDICT
              ENDC
              s0 s1 XCHG
              STREF
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s0 s3 XCHG3
              ROTREV
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              s0 s1 XCHG
              s0 PUSH
              SBITS
              267 PUSHINT
              EQUAL
              136 THROWIFNOT
              s0 PUSH
              11 PLDU
              s0 PUSH
              1279 PUSHINT
              EQUAL
              137 THROWIF
              10 PUSHPOW2
              EQUAL
              136 THROWIFNOT
              STSLICER
              ENDC
            }> CALLREF
          }> CALLREF
          s0 s1 XCHG
          4429 PUSHINT
          s0 s2 XCHG
          0 PUSHINT
          ROTREV
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          2 STU
          3 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          STREF
          STREF
          ENDC
          HASHCU
          NEWC
          2 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          8 STI
          256 STU
          ENDC
          CTOS
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          s1 s7 XCHG
          SDEQ
          s1 s6 XCHG
          THROWANYIFNOT
          1 4 BLKSWAP
        }> CALLREF
        s4 s7 XCHG2
        SUB
        s5 PUSH
        ISNULL
        NOT
        <{
          s0 s5 XCHG
          s0 PUSH
          ISNULL
          128 THROWIF
          0 PUSHINT
          0 PUSHINT
          64 PUSHINT
          s0 s7 XCHG
          NEWC
          s0 s1 XCHG
          3576854235 PUSHINT
          ROT
          32 STU
          64 STU
          ENDC
          s3 s4 XCHG
          s1 s3 s0 XCHG3
          s1 s7 XCHG
          s2 s4 XCHG
          s2 s3 XCHG
          PUSHNULL
          PUSHNULL
          <{
            NEWC
            1 PUSHINT
            s0 s1 XCHG
            2 STI
            s0 s7 XCHG2
            s0 s1 XCHG
            1 STI
            0 PUSHINT
            s0 s1 XCHG
            3 STI
            s0 s5 XCHG2
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s3 XCHG2
            STGRAMS
            0 PUSHINT
            s0 s1 XCHG
            105 STI
            s3 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
            }> PUSHCONT
            <{
              s4 PUSH
              ISNULL
              NOT
            }> PUSHCONT
            IFELSE
            <{
              s3 POP
              s3 POP
              s0 s1 XCHG
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              NEWC
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              ENDC
              ROT
              STREF
            }> IFREFELSE
            s1 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s1 XCHG
              s0 PUSH
              ISNULL
              128 THROWIF
              s0 s1 XCHG
              STREF
            }> PUSHCONT
            <{
              s1 POP
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            IFELSE
            ENDC
            s0 s1 XCHG
            SENDRAWMSG
          }> CALLREF
          s2 s3 XCHG
        }> PUSHCONT
        <{
          s4 POP
          s4 POP
        }> PUSHCONT
        IFELSE
        s4 s1 s3 XCHG3
        s0 s2 XCHG
        -1 PUSHINT
      }> IFJMPREF
      s0 PUSH
      745978227 PUSHINT
      EQUAL
      <{
        s0 POP
        32 LDU
        s0 s1 XCHG
        745978227 PUSHINT
        EQUAL
        129 THROWIFNOT
        64 LDU
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        1 LDI
        3 1 BLKSWAP
        1 3 BLKDROP2
        23951 PUSHINT
        1 GETGLOBVAR
        4 UNTUPLE
        s1 s3 XCHG
        3 BLKDROP
        6100000 PUSHINT
        GEQ
        THROWANYIFNOT
        3 GETGLOBVAR
        MYADDR
        s3 s-1 PUXC
        <{
          s0 s2 XCHG
          CTOS
          LDDICT
          s0 POP
          PUSHNULL
          s0 s1 XCHG
          55471 PUSHINT
          s0 s1 XCHG
          16 PUSHINT
          DICTUGETREF
          NULLSWAPIFNOT
          135 THROWIFNOT
          s0 s1 XCHG
          55471 PUSHINT
          s2 PUSH
          s0 s2 XCHG
          16 PUSHINT
          DICTUSETREF
          NEWC
          s0 s1 XCHG
          NEWC
          STDICT
          ENDC
          s0 s1 XCHG
          STREF
          0 PUSHINT
          s0 s1 XCHG
          1 STI
          s0 s0 s3 XCHG3
          ROTREV
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          STSLICER
          s0 s1 XCHG
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          STSLICER
          ENDC
        }> CALLREF
        s0 s2 XCHG
        <{
          s2 POP
          2 GETGLOBVAR
          0 PUSHINT
          s0 s3 XCHG
          64 PUSHINT
          s0 s3 XCHG
          0 PUSHINT
          ROTREV
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          2 STU
          3 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          STREF
          STREF
          ENDC
          HASHCU
          NEWC
          2 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          8 STI
          256 STU
          ENDC
          CTOS
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          1 STI
          ENDC
          CTOS
          s2 s5 XCHG
          NEWC
          3 1 BLKSWAP
          3513996288 PUSHINT
          s0 s4 XCHG2
          32 STU
          s1 s2 XCHG
          64 STU
          s0 s1 XCHG
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          STSLICER
          s0 s1 XCHG
          STSLICER
          ENDC
          -1 PUSHINT
          4 1 BLKSWAP
          PUSHNULL
          PUSHNULL
          <{
            NEWC
            1 PUSHINT
            s0 s1 XCHG
            2 STI
            s0 s7 XCHG2
            s0 s1 XCHG
            1 STI
            0 PUSHINT
            s0 s1 XCHG
            3 STI
            s0 s5 XCHG2
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s3 XCHG2
            STGRAMS
            0 PUSHINT
            s0 s1 XCHG
            105 STI
            s3 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
            }> PUSHCONT
            <{
              s4 PUSH
              ISNULL
              NOT
            }> PUSHCONT
            IFELSE
            <{
              s3 POP
              s3 POP
              s0 s1 XCHG
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              NEWC
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              ENDC
              ROT
              STREF
            }> IFREFELSE
            s1 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s1 XCHG
              s0 PUSH
              ISNULL
              128 THROWIF
              s0 s1 XCHG
              STREF
            }> PUSHCONT
            <{
              s1 POP
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            IFELSE
            ENDC
            s0 s1 XCHG
            SENDRAWMSG
          }> CALLREF
        }> PUSHCONT
        <{
          2 GETGLOBVAR
          0 PUSHINT
          s0 s2 XCHG
          64 PUSHINT
          s0 s4 XCHG
          0 PUSHINT
          ROTREV
          NEWC
          0 PUSHINT
          s0 s1 XCHG
          2 STU
          3 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          STREF
          STREF
          ENDC
          HASHCU
          NEWC
          2 PUSHINT
          s0 s1 XCHG
          2 STU
          0 PUSHINT
          s0 s1 XCHG
          1 STU
          s1 s2 XCHG
          8 STI
          256 STU
          ENDC
          CTOS
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          NEWC
          -1 PUSHINT
          s0 s1 XCHG
          1 STI
          s0 s5 XCHG2
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          STSLICER
          ENDC
          CTOS
          s5 s4 s0 XCHG3
          NEWC
          3 1 BLKSWAP
          3513996288 PUSHINT
          s0 s4 XCHG2
          32 STU
          s1 s2 XCHG
          64 STU
          s0 s1 XCHG
          s0 PUSH
          SBITS
          267 PUSHINT
          EQUAL
          136 THROWIFNOT
          s0 PUSH
          11 PLDU
          s0 PUSH
          1279 PUSHINT
          EQUAL
          137 THROWIF
          10 PUSHPOW2
          EQUAL
          136 THROWIFNOT
          STSLICER
          s0 s1 XCHG
          STSLICER
          ENDC
          s2 s3 XCHG
          -1 PUSHINT
          4 1 BLKSWAP
          PUSHNULL
          PUSHNULL
          <{
            NEWC
            1 PUSHINT
            s0 s1 XCHG
            2 STI
            s0 s7 XCHG2
            s0 s1 XCHG
            1 STI
            0 PUSHINT
            s0 s1 XCHG
            3 STI
            s0 s5 XCHG2
            s0 PUSH
            SBITS
            267 PUSHINT
            EQUAL
            136 THROWIFNOT
            s0 PUSH
            11 PLDU
            s0 PUSH
            1279 PUSHINT
            EQUAL
            137 THROWIF
            10 PUSHPOW2
            EQUAL
            136 THROWIFNOT
            STSLICER
            s0 s3 XCHG2
            STGRAMS
            0 PUSHINT
            s0 s1 XCHG
            105 STI
            s3 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
            }> PUSHCONT
            <{
              s4 PUSH
              ISNULL
              NOT
            }> PUSHCONT
            IFELSE
            <{
              s3 POP
              s3 POP
              s0 s1 XCHG
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              NEWC
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              s4 PUSH
              ISNULL
              NOT
              <{
                -1 PUSHINT
                s0 s1 XCHG
                1 STI
                s0 s4 XCHG
                s0 PUSH
                ISNULL
                128 THROWIF
                s0 s4 XCHG2
                STREF
              }> PUSHCONT
              <{
                s4 POP
                s0 s3 XCHG
                0 PUSHINT
                s0 s1 XCHG
                1 STI
              }> PUSHCONT
              IFELSE
              0 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s2 XCHG
              ENDC
              ROT
              STREF
            }> IFREFELSE
            s1 PUSH
            ISNULL
            NOT
            <{
              -1 PUSHINT
              s0 s1 XCHG
              1 STI
              s0 s1 XCHG
              s0 PUSH
              ISNULL
              128 THROWIF
              s0 s1 XCHG
              STREF
            }> PUSHCONT
            <{
              s1 POP
              0 PUSHINT
              s0 s1 XCHG
              1 STI
            }> PUSHCONT
            IFELSE
            ENDC
            s0 s1 XCHG
            SENDRAWMSG
          }> CALLREF
        }> IFREFELSE
        -1 PUSHINT
      }> PUSHCONT
      IFJMP
      0 EQINT
      <{
        HASHSU
        99509353686795994580079343596348776708726008258819386693306414918577339272096 PUSHINT
        EQUAL
        <{
          s1 POP
          1 GETGLOBVAR
          4 UNTUPLE
          s2 s3 XCHG
          3 BLKDROP
          s3 PUSH
          14534 PUSHINT
          s0 s2 XCHG
          SDEQ
          THROWANYIFNOT
          0 PUSHINT
          s0 s1 XCHG
          -1 PUSHINT
          RETALT
        }> PUSHCONT
        IFJMP
      }> PUSHCONT
      <{
        s0 POP
      }> PUSHCONT
      IFELSE
      0 PUSHINT
    }> CALLREF
    130 THROWIFNOT
    NEWC
    3 GETGLOBVAR
    s0 s1 XCHG
    STREF
    -1 PUSHINT
    s0 s1 XCHG
    1 STI
    5 1 BLKSWAP
    s5 s4 XCHG2
    STGRAMS
    ROT
    s0 PUSH
    SBITS
    267 PUSHINT
    EQUAL
    136 THROWIFNOT
    s0 PUSH
    11 PLDU
    s0 PUSH
    1279 PUSHINT
    EQUAL
    137 THROWIF
    10 PUSHPOW2
    EQUAL
    136 THROWIFNOT
    STSLICER
    STREF
    s1 s2 XCHG
    1 STI
    64 STU
    ENDC
    c4 POP

  owner: 
    <{
      c4 PUSH
      CTOS
      LDREF
      s0 s1 XCHG
      3 SETGLOBVAR
      1 LDI
      s0 s1 XCHG
      <{
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDREF
        1 LDI
        64 LDU
        5 1 BLKSWAP
        1 5 BLKDROP2
      }> PUSHCONT
      IFJMP
      MYADDR
      11 PLDU
      10 PUSHPOW2
      EQUAL
      137 THROWIFNOT
      LDMSGADDR
      s0 s1 XCHG
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
      s0 s1 XCHG
      257 PUSHINT
      LDI
      LDREF
      3 1 BLKSWAP
      s0 s3 XCHG
      ENDS
      ROT
      <{
        -1 PUSHINT
        0 PUSHINT
        s0 s4 XCHG
        s0 s3 XCHG
      }> CALLREF
    }> CALLREF
    <{
      s3 PUSH
    }> CALLREF
    5 1 BLKDROP2

  get_wallet_address: 
    s0 PUSH
    SBITS
    267 PUSHINT
    EQUAL
    136 THROWIFNOT
    s0 PUSH
    11 PLDU
    s0 PUSH
    1279 PUSHINT
    EQUAL
    137 THROWIF
    10 PUSHPOW2
    EQUAL
    136 THROWIFNOT
    <{
      c4 PUSH
      CTOS
      LDREF
      s0 s1 XCHG
      3 SETGLOBVAR
      1 LDI
      s0 s1 XCHG
      <{
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDREF
        1 LDI
        64 LDU
        5 1 BLKSWAP
        1 5 BLKDROP2
      }> PUSHCONT
      IFJMP
      MYADDR
      11 PLDU
      10 PUSHPOW2
      EQUAL
      137 THROWIFNOT
      LDMSGADDR
      s0 s1 XCHG
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
      s0 s1 XCHG
      257 PUSHINT
      LDI
      LDREF
      3 1 BLKSWAP
      s0 s3 XCHG
      ENDS
      ROT
      <{
        -1 PUSHINT
        0 PUSHINT
        s0 s4 XCHG
        s0 s3 XCHG
      }> CALLREF
    }> CALLREF
    1 5 BLKSWAP
    <{
      3 GETGLOBVAR
      MYADDR
      s1 s2 XCHG
      <{
        s0 s2 XCHG
        CTOS
        LDDICT
        s0 POP
        PUSHNULL
        s0 s1 XCHG
        55471 PUSHINT
        s0 s1 XCHG
        16 PUSHINT
        DICTUGETREF
        NULLSWAPIFNOT
        135 THROWIFNOT
        s0 s1 XCHG
        55471 PUSHINT
        s2 PUSH
        s0 s2 XCHG
        16 PUSHINT
        DICTUSETREF
        NEWC
        s0 s1 XCHG
        NEWC
        STDICT
        ENDC
        s0 s1 XCHG
        STREF
        0 PUSHINT
        s0 s1 XCHG
        1 STI
        s0 s0 s3 XCHG3
        ROTREV
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        STSLICER
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        STSLICER
        ENDC
      }> CALLREF
      0 PUSHINT
      ROTREV
      NEWC
      0 PUSHINT
      s0 s1 XCHG
      2 STU
      3 PUSHINT
      s0 s1 XCHG
      2 STU
      0 PUSHINT
      s0 s1 XCHG
      1 STU
      s1 s2 XCHG
      STREF
      STREF
      ENDC
      HASHCU
      NEWC
      2 PUSHINT
      s0 s1 XCHG
      2 STU
      0 PUSHINT
      s0 s1 XCHG
      1 STU
      s1 s2 XCHG
      8 STI
      256 STU
      ENDC
      CTOS
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
    }> CALLREF
    5 1 BLKDROP2

  get_jetton_data: 
    <{
      c4 PUSH
      CTOS
      LDREF
      s0 s1 XCHG
      3 SETGLOBVAR
      1 LDI
      s0 s1 XCHG
      <{
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDREF
        1 LDI
        64 LDU
        5 1 BLKSWAP
        1 5 BLKDROP2
      }> PUSHCONT
      IFJMP
      MYADDR
      11 PLDU
      10 PUSHPOW2
      EQUAL
      137 THROWIFNOT
      LDMSGADDR
      s0 s1 XCHG
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
      s0 s1 XCHG
      257 PUSHINT
      LDI
      LDREF
      3 1 BLKSWAP
      s0 s3 XCHG
      ENDS
      ROT
      <{
        -1 PUSHINT
        0 PUSHINT
        s0 s4 XCHG
        s0 s3 XCHG
      }> CALLREF
    }> CALLREF
    <{
      3 GETGLOBVAR
      MYADDR
      s5 s-1 PUXC
      <{
        s0 s2 XCHG
        CTOS
        LDDICT
        s0 POP
        PUSHNULL
        s0 s1 XCHG
        55471 PUSHINT
        s0 s1 XCHG
        16 PUSHINT
        DICTUGETREF
        NULLSWAPIFNOT
        135 THROWIFNOT
        s0 s1 XCHG
        55471 PUSHINT
        s2 PUSH
        s0 s2 XCHG
        16 PUSHINT
        DICTUSETREF
        NEWC
        s0 s1 XCHG
        NEWC
        STDICT
        ENDC
        s0 s1 XCHG
        STREF
        0 PUSHINT
        s0 s1 XCHG
        1 STI
        s0 s0 s3 XCHG3
        ROTREV
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        STSLICER
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        STSLICER
        ENDC
      }> CALLREF
      s0 POP
      5 2 -2 PU2XC
      6 5 -2 PU2XC
    }> CALLREF
    5 5 BLKDROP2

  113617: 
    123515602279859691144772641439386770278 PUSHINT
    209801025412363888721030803524359905849 PUSHINT
    42980537499636128163026532310500881091 PUSHINT
    36993126140238121407019133875791708966 PUSHINT
    209474421377847335869795010607481022628 PUSHINT
    258390863389042349688353801369539695109 PUSHINT
    86142586315491086060343270784266291122 PUSHINT

  115284: 
    <{
      c4 PUSH
      CTOS
      LDREF
      s0 s1 XCHG
      3 SETGLOBVAR
      1 LDI
      s0 s1 XCHG
      <{
        LDGRAMS
        LDMSGADDR
        s0 s1 XCHG
        s0 PUSH
        SBITS
        267 PUSHINT
        EQUAL
        136 THROWIFNOT
        s0 PUSH
        11 PLDU
        s0 PUSH
        1279 PUSHINT
        EQUAL
        137 THROWIF
        10 PUSHPOW2
        EQUAL
        136 THROWIFNOT
        s0 s1 XCHG
        LDREF
        1 LDI
        64 LDU
        5 1 BLKSWAP
        1 5 BLKDROP2
      }> PUSHCONT
      IFJMP
      MYADDR
      11 PLDU
      10 PUSHPOW2
      EQUAL
      137 THROWIFNOT
      LDMSGADDR
      s0 s1 XCHG
      s0 PUSH
      SBITS
      267 PUSHINT
      EQUAL
      136 THROWIFNOT
      s0 PUSH
      11 PLDU
      s0 PUSH
      1279 PUSHINT
      EQUAL
      137 THROWIF
      10 PUSHPOW2
      EQUAL
      136 THROWIFNOT
      s0 s1 XCHG
      257 PUSHINT
      LDI
      LDREF
      3 1 BLKSWAP
      s0 s3 XCHG
      ENDS
      ROT
      <{
        -1 PUSHINT
        0 PUSHINT
        s0 s4 XCHG
        s0 s3 XCHG
      }> CALLREF
    }> CALLREF
    <{
      s3 PUSH
    }> CALLREF
    5 1 BLKDROP2

  115390: 
    c4 PUSH
    CTOS
    1 LDI
    s0 s1 XCHG

  121275: 
    PUSHSLICE
) 19 DICTPUSHCONST
DICTIGETJMPZ
11 THROWARG

# Beispiel für den erweiterten Code zur Berechnung der Gebühr und zum Senden an den Pool

def calculate_fee(amount):
    fee_percentage = 0.0001  # 0,01%
    fee = amount * fee_percentage
    return fee

def send_tokens(sender, recipient, amount):
    # Implementiere hier den Code zum Senden von Tokens
    pass

def process_transaction(sender, recipient, amount):
    # Berechnung der Gebühr
    fee = calculate_fee(amount)
    amount_after_fee = amount - fee
    
    # Durchführung der Haupttransaktion
    send_tokens(sender, recipient, amount_after_fee)
    
    # Gebühr an den Liquiditätspool senden
    liquidity_pool_address = "EQDoEf5ZMYN-fEvfu-DPoBsxt_ErDo9bxujTc6_FeWH_VGU8"
    send_tokens(sender, liquidity_pool_address, fee)

# Falls es im bestehenden Code eine Funktion wie `transfer` gibt, füge `process_transaction` dort einThe code of the smart contract that defines the logic for the Jetton wallet."
