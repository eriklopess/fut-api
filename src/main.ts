import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify';
import fastifyHelmet from '@fastify/helmet';
import { WinstonModule } from 'nest-winston';
import { winstonConfig } from './shared/config/logger.config';

async function bootstrap() {
  const fastifyAdapter = new FastifyAdapter();
  const logger = WinstonModule.createLogger(winstonConfig);
  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    fastifyAdapter,
    {
      logger,
    },
  );
  await app.register(fastifyHelmet);
  await app.listen(3000);
}
bootstrap();
