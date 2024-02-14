import useGames from '@/hooks/useGames'
import { Team } from '@/types/teams'
import { Center, List, Loader, ThemeIcon, rem, Title } from '@mantine/core'
import { IconSoccerField } from '@tabler/icons-react'

type Props = {
  firstTeam: Team
  secondTeam: Team
}

export default function GameHistoryList({ firstTeam, secondTeam }: Props) {
  const { isLoading, data } = useGames(firstTeam.id, secondTeam.id)

  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    return (
      <>
        <Title order={4} ta="center" m="lg">
          History
        </Title>
        <Center>
          <List
            spacing="xs"
            size="sm"
            center
            icon={
              <ThemeIcon color="teal" size={24} radius="xl">
                <IconSoccerField style={{ width: rem(16), height: rem(16) }} />
              </ThemeIcon>
            }
          >
            {data.map((game) => (
              <List.Item key={game.id}>
                {game.first_team_goals} - {game.second_team_goals}
              </List.Item>
            ))}
          </List>
        </Center>
      </>
    )
  }
  return <></>
}
