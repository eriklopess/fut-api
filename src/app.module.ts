import { Module } from '@nestjs/common';
import { TeamsModule } from './teams/teams.module';
import { WinstonModule } from 'nest-winston';
import { winstonConfig } from './shared/config/logger.config';
import { LoggerInterceptor } from './shared/interceptors/Logger.Interceptor';
import { ThrottlerGuard, ThrottlerModule } from '@nestjs/throttler';

@Module({
  imports: [
    TeamsModule,
    WinstonModule.forRoot(winstonConfig),
    ThrottlerModule.forRoot([
      {
        ttl: 100,
        limit: 10,
      },
    ]),
  ],
  controllers: [],
  providers: [
    {
      provide: 'APP_INTERCEPTOR',
      useValue: LoggerInterceptor,
    },
    {
      provide: 'APP_GUARD',
      useClass: ThrottlerGuard,
    },
  ],
})
export class AppModule {}
