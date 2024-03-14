import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify';
import fastifyHelmet from '@fastify/helmet';
import { WinstonModule } from 'nest-winston';
import { winstonConfig } from './shared/config/logger.config';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

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

  const config = new DocumentBuilder()
    .setTitle('fut-api')
    .setDescription('The fut-api API description')
    .setVersion('1.0')
    .addTag('fut-api')
    .build();

  const document = SwaggerModule.createDocument(app, config);

  SwaggerModule.setup('api', app, document);

  await app.register(fastifyHelmet);
  await app.listen(3000);
}
bootstrap();
