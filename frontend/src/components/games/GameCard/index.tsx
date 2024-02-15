import { Game } from '@/types/games'
import { Card, Group, Text, Stack } from '@mantine/core'
import TeamBadge from '@/components/teams/TeamBadge'

type Props = {
  game: Game
}

export default function GameCard({ game }: Props) {
  return (
    <Card withBorder p="xl" radius="md" data-testid="game-card">
      <Group>
        <div>
          <Stack>
            <Group justify="center" gap="lg" grow>
              <Stack>
                <Text size="xl" fw={700} ta={'center'}>
                  {game.first_team.name}
                </Text>
                <Text size="lg" ta={'center'}>
                  {game.first_team_goals}
                </Text>
              </Stack>
              <Text size="xl" fw={700} ta={'center'}>
                vs
              </Text>
              <Stack>
                <Text size="xl" fw={700} ta={'center'}>
                  {game.second_team?.name}
                </Text>
                <Text size="lg" ta={'center'}>
                  {game.second_team_goals}
                </Text>
              </Stack>
            </Group>
            <div>
              <Text fz="md" mb={6}>
                {game.first_team.name}
              </Text>
              <TeamBadge
                firstPlayer={game.first_team.first_player}
                secondPlayer={game.first_team.second_player}
              />
            </div>
            {game.second_team && (
              <div>
                <Text fz="md" mb={6}>
                  {game.second_team?.name}
                </Text>
                <TeamBadge
                  firstPlayer={game.second_team.first_player}
                  secondPlayer={game.second_team.second_player}
                />
              </div>
            )}
          </Stack>
        </div>
      </Group>
    </Card>
  )
}
