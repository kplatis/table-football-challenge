import { Game } from '@/types/games'
import { Card, Group, Text, Stack, Title, Center } from '@mantine/core'
import classes from './GamesCard.module.css'

type Props = {
  game: Game
}

export default function GameCard({ game }: Props) {
  return (
    <Card withBorder padding="lg" className={classes.card}>
      <Center>
        <Title order={3}>
          {game.first_team.name} vs {game.second_team.name}
        </Title>
      </Center>
      <Text mt="sm" mb="md" c="dimmed" fz="xs">
        HERE ADD THE PLAYERS
      </Text>
      <Card.Section className={classes.footer}>
        <Stack>
          <Center>
            <Group>
              <div>{game.first_team_goals}</div>
              <div>-</div>
              <div>{game.second_team_goals}</div>
            </Group>
          </Center>
        </Stack>
      </Card.Section>
    </Card>
  )
}
