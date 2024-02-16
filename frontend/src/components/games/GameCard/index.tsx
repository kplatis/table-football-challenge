import { Game } from '@/types/games'
import { Card, Group, Text, Stack, Center, Title } from '@mantine/core'
import PlayerBadge from '@/components/players/PlayerBadge'

type Props = {
  game: Game
}

export default function GameCard({ game }: Props) {
  return (
    <Card withBorder p="lg" radius="md" data-testid="game-card">
      <Center>
        <Group justify="space-between" gap="sm">
          <Stack>
            <Title order={3} fw={700} ta={'center'}>
              {game.first_team.name}
            </Title>
            <Title order={4} fw={700} ta={'center'}>
              {game.first_team_goals}
            </Title>

            <Stack mt="md">
              <PlayerBadge name={game.first_team.first_player.name} />
              {game.first_team.second_player && (
                <PlayerBadge name={game.first_team.second_player.name} />
              )}
            </Stack>
          </Stack>
          <Text size="xl" fw={700} ta={'center'}>
            vs
          </Text>
          <Stack>
            <Title order={3} fw={700} ta={'center'}>
              {game.second_team.name}
            </Title>
            <Title order={4} fw={700} ta={'center'}>
              {game.second_team_goals}
            </Title>

            <Stack mt="md">
              <PlayerBadge name={game.second_team.first_player.name} />
              {game.second_team.second_player && (
                <PlayerBadge name={game.second_team.second_player.name} />
              )}
            </Stack>
          </Stack>
        </Group>
      </Center>
    </Card>
  )
}
