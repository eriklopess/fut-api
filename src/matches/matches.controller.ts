import { Controller, Get } from '@nestjs/common';

@Controller('matches')
export class MatchesController {
  @Get()
  findAll(): string {
    return 'This action returns all next matches';
  }
}
