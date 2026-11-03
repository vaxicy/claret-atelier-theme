
// Claret Atelier Theme — deep claret, warm brass and cool grey blue
import { readFile } from 'node:fs/promises';

const ATELIER_PALETTE = {
  claret: '#8A1A2C',
  deepClaret: '#5A0F1E',
  brass: '#D8BC8C',
  paper: '#FAF6EE',
  greyBlue: '#9FB4C6',
};

export class PigmentMixer {
  constructor(studio = 'North studio') {
    this.studio = studio;
    this.palette = ATELIER_PALETTE;
  }

  /** Mix two pigment colors into a tinted shade. */
  mix(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readRecipe(file) {
    const content = await readFile(file, 'utf8');
    const steps = content.split('\n').filter(Boolean);
    return {
      studio: this.studio,
      pigments: Object.keys(this.palette).length,
      steps: steps.length,
      content,
    };
  }
}

const mixer = new PigmentMixer();
const wash = mixer.mix(ATELIER_PALETTE.claret, ATELIER_PALETTE.paper);

console.log(`wash shade: ${wash}`);
