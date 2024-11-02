let blocks = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'.split(', ');

//            x  y
let coords = [0, 0];
let direction = 'n';

for (let block of blocks) {
    if (block[0] === 'L')
        turn_left();
    else if (block[0] === 'R')
        turn_right();
    move(parseInt(block.replace(block[0],'')))
}

console.log(`blocks: ${coords[0] + coords[1]}`)

function move(moves) {
    switch (direction) {
        case 'n':
            coords[1] += moves;
            break;
        case 'o':
            coords[0] += moves;
            break;
        case 's':
            coords[1] -= moves;
            break;
        case 'e': 
            coords[0] -= moves;
            break;
    }
}

function turn_left() {
    switch (direction) {
        case 'n':
            direction = 'o';
            break;
        case 'o':
            direction = 's';
            break;
        case 's':
            direction = 'e';
            break;
        case 'e': 
            direction = 'n';
            break;
    }
}

function turn_right() {
    switch (direction) {
        case 'n':
            direction = 'e';
            break;
        case 'e':
            direction = 's';
            break;
        case 's':
            direction = 'o';
            break;
        case 'o':
            direction = 'n';
    }
}