

int romanToInt(char * s){
    int map[26], ret = 0;
    map['I' - 'A'] = 1;
    map['V' - 'A'] = 5;
    map['X' - 'A'] = 10;
    map['L' - 'A'] = 50;
    map['C' - 'A'] = 100;
    map['D' - 'A'] = 500;
    map['M' - 'A'] = 1000;
    
    while (*s) {
        if (!s[1]) {
            ret += map[s[0] - 'A'];
            break;
        }
        
        if (map[s[0] - 'A'] < map[s[1] - 'A']) {
            ret += map[s[1] - 'A'] - map[s[0] - 'A'];
            s += 2;
        } else {
            ret += map[s[0] - 'A'];
            s += 1;
        }
    }
    
    return ret;
}

