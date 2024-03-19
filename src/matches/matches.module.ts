import { Module } from '@nestjs/common';
import { MatchesController } from './matches.controller';
import { MatchesServices } from './matches.service';

@Module({
  imports: [],
  controllers: [MatchesController],
  providers: [MatchesServices],
})
export class MatchesModule {}
