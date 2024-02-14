import useStatistics from '@/hooks/useStatistics'
import { StatisticsCategory } from '@/types/statistics'
import { Team } from '@/types/teams'
import { Center, Loader, Text } from '@mantine/core'

type Props = {
  firstTeam: Team
  secondTeam: Team
}

export default function StatisticsScore({ firstTeam, secondTeam }: Props) {
  const { isLoading, data } = useStatistics(
    StatisticsCategory.Teams,
    firstTeam.id,
    secondTeam.id,
  )
  if (isLoading) {
    return (
      <Center>
        <Loader />
      </Center>
    )
  }
  if (data) {
    // TODO: add id in stats
    const stats = data.find((stat) => stat.name === firstTeam.name)

    let sentence = ''

    if (stats) {
      const { wins, losses } = stats

      if (wins > losses) {
        sentence = `${firstTeam.name} wins in direct confrontations with ${secondTeam.name}: ${wins} - ${losses}`
      } else if (wins < losses) {
        sentence = `${firstTeam.name} loses in direct confrontations with ${secondTeam.name}: ${wins} - ${losses}`
      } else {
        sentence = `${firstTeam.name} and ${secondTeam.name} are draw: ${wins} - ${losses}`
      }
    } else {
      sentence = 'There are no games between the two team'
    }

    return (
      <Center m="xl">
        <Text>{sentence}</Text>{' '}
      </Center>
    )
  }
  return null
}
