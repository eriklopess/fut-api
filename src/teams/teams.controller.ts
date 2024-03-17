import { Controller, Get } from '@nestjs/common';

@Controller('teams')
export class TeamsController {
  @Get()
  findAll(): string {
    return 'This action returns all teams';
  }
}
