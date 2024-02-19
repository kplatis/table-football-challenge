'use client'

import { Overlay, Container, Title, Button, Text, Group } from '@mantine/core'
import classes from './HeroPage.module.css'
import { useRouter } from 'next/navigation'

export function HeroPage() {
  const router = useRouter()

  return (
    <div className={classes.hero}>
      <Overlay
        gradient="linear-gradient(180deg, rgba(0, 0, 0, 0.25) 0%, rgba(0, 0, 0, .65) 40%)"
        opacity={1}
        zIndex={0}
      />
      <Container
        className={classes.container}
        size="md"
        h={'calc(100vh - 76px)'}
      >
        <Title className={classes.title}>Table football challenge</Title>
        <Text className={classes.description} size="xl" mt="xl">
          Organize Players, Form Teams, Record Matches, and Keep Score with
          Precision! Your All-in-One Solution for Table Football Management
        </Text>
        <Group>
          <Button
            variant="gradient"
            size="xl"
            radius="xl"
            className={classes.control}
            onClick={() => router.push('/teams')}
          >
            List the teams
          </Button>
          <Button
            variant="gradient"
            size="xl"
            radius="xl"
            className={classes.control}
            onClick={() => router.push('/games')}
          >
            List the games
          </Button>
          <Button
            variant="gradient"
            size="xl"
            radius="xl"
            className={classes.control}
            onClick={() => router.push('/dashboard')}
          >
            Check statistics
          </Button>
        </Group>
      </Container>
    </div>
  )
}
