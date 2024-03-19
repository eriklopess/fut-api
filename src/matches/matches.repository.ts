import { PrismaService } from 'src/shared/db/Prisma.service';
import { default as rounds } from '../../data/rodada.json';

export class MatchesRepository {
  constructor(private readonly prisma: PrismaService) {}

  async dump() {
    if (rounds)
      for (const round of rounds.rounds) {
        await this.prisma.match.create({
          data: {
            id: round.id,
            at: round.date,
            home: round.home,
            away: round.away,
          },
        });
      }
  }
}
