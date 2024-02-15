import { Button, Card, Center, Group, Stack, Title } from '@mantine/core'
import { FirstOrSecond, GameState } from './types'

type Props = {
  game: GameState
  teamScoredFn: (firstOrSecond: FirstOrSecond) => void
  gameFinishedFn: () => void
}

export default function LiveGame({
  game,
  teamScoredFn,
  gameFinishedFn,
}: Props) {
  return (
    <Center>
      <Stack gap={'lg'}>
        <Card withBorder radius={'md'} p={'xl'} mt={'xl'} data-testid="live-game-card">
          <Group>
            <Stack gap={'lg'}>
              <Title order={2}>{game.firstTeam?.name}</Title>
              <Title order={4} ta="center">
                {game.firstTeamGoals}
              </Title>
              <Button onClick={() => teamScoredFn(FirstOrSecond.First)}>
                Score!
              </Button>
            </Stack>
            <Stack gap={'lg'}>
              <Title order={2}>{game.secondTeam?.name}</Title>
              <Title order={4} ta="center">
                {game.secondTeamGoals}
              </Title>
              <Button onClick={() => teamScoredFn(FirstOrSecond.Second)}>
                Score!
              </Button>
            </Stack>
          </Group>
        </Card>
        <Button onClick={() => gameFinishedFn()} data-testid="submit-game-button">Submit Game</Button>
      </Stack>
    </Center>
  )
}
