import GamesGrid from '@/components/games/GamesGrid'
import { Stack, Title } from '@mantine/core'

export default function GamesPage() {
  return (
    <Stack gap="lg">
      <Title order={1} ta="center" m="xl">
        Games
      </Title>

      <GamesGrid />
    </Stack>
  )
}
