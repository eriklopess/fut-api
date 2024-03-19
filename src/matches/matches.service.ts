import { Injectable } from '@nestjs/common';

@Injectable()
export class MatchesServices {
  findAll(): string {
    return 'This action returns all next matches';
  }
}
