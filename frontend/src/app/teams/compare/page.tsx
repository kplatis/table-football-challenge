import TeamComparison from '@/components/teams/TeamComparison'
import { Title } from '@mantine/core'

export default function TeamComparisonPage() {
  return (
    <>
      <Title order={1} ta="center" mb="xl">
        Compare Teams
      </Title>
      <TeamComparison />
    </>
  )
}
