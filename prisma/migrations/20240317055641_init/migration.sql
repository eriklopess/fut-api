-- CreateTable
CREATE TABLE "MatchModel" (
    "id" TEXT NOT NULL,
    "at" TIMESTAMP(3) NOT NULL,
    "home" TEXT NOT NULL,
    "away" TEXT NOT NULL,

    CONSTRAINT "MatchModel_pkey" PRIMARY KEY ("id")
);
