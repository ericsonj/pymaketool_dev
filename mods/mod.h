#ifndef _MODS_MOD_H_PY_
#define _MODS_MOD_H_PY_
#define DECL_MOD      _MODULE(mod)
#define DECL_MOD2     _MODULE(mod2)
/**
 * 
 * Key map
 * 
 */
enum {
    KEY_1 = 1,
    KEY_2,
    KEY_3,
    KEY_4,
    KEY_5,
    KEY_6,
    KEY_7,
    KEY_8,
    KEY_9,
    KEY_10,
    KEY_11,
    KEY_12,
    KEY_13,
    KEY_14,
    KEY_15,
    KEY_16,
    KEY_17,
    KEY_18,
    KEY_19,
};
enum {
    HTTP_200 = 0,
};
#define HTTP_REQUEST_VALUES  =\
    {\
        "OK",\
    }
    

#ifndef DECL_HTTP_REQUEST
#define _DECL extern
#define _VAR
#else
#define _DECL
#define _VAR  HTTP_REQUEST_VALUES
#endif
    

_DECL char* HTTP_REQUEST[1] _VAR;
    
#endif // _MODS_MOD_H_PY_
